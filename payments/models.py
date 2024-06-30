import uuid

from django.db import models


class Payment(models.Model):
    payment_id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False
    )
    sender_address = models.CharField(max_length=256)
    receiver_address = models.CharField(max_length=256)
    amount = models.FloatField()
    payment_datetime = models.DateTimeField()
    status = models.CharField(
        max_length=256,
        choices=(("INPROGRESS", "INPROGRESS"), ("COMPLETE", "COMPLETE")),
    )
    payment_type = models.CharField(
        max_length=256,
        choices=(("SCHEDULED", "SCHEDULED"), ("LOCKED", "LOCKED")),
    )

    class Meta:
        db_table = "payment"
        verbose_name_plural = "payments"
        ordering = ["-payment_datetime"]
