from letapay_backend.celery import app
from payments.models import Payment


@app.task
def make_payment(payment_id):
    p = Payment.objects.get(payment_id=payment_id)
    p.status = "COMPLETE"
    p.save()
    print(payment_id)


def schedule_task_at_specific_time(payment_id, payment_datetime):
    print(f"{payment_id} -- {payment_datetime}")
    make_payment.apply_async(args=[payment_id], eta=payment_datetime)
