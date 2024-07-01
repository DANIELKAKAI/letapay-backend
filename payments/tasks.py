from letapay_backend.celery import app
from payments.models import Payment
from payments.web3_utils import complete_payment, get_payment


@app.task
def make_payment(payment_id):
    payment = get_payment(payment_id)
    if payment[0] == "":
        return
    tx_receipt = complete_payment(payment_id)
    if tx_receipt:
        p = Payment.objects.get(payment_id=payment_id)
        p.status = "COMPLETE"
        p.save()
        return True


def schedule_task_at_specific_time(payment_id, payment_datetime):
    print(f"{payment_id} -- {payment_datetime}")
    make_payment.apply_async(args=[payment_id], eta=payment_datetime)
