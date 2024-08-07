from django.db import models
from django.core.validators import MinValueValidator
from uuid import uuid4

from reservation.models import Reservation


# Create your models here.
class Payment(models.Model):
    res_obj = models.ForeignKey(
        Reservation,
        on_delete=models.CASCADE,
        related_name="res_id",
        blank=True,
        null=True,
    )

    reserv_id = models.CharField(max_length=20)

    class StatusChoices(models.TextChoices):
        READY = "ready", "미결제"
        PAID = "paid", "결제완료"
        CANCELLED = "cancelled", "결제취소"
        FAILED = "failed", "결제실패"

    uid = models.UUIDField(default=uuid4, editable=False)
    name = models.CharField(max_length=100)
    amount = models.PositiveIntegerField(
        validators=[
            MinValueValidator(1, message="1원 이상의 금액을 지정해주세요."),
        ]
    )
    status = models.CharField(
        max_length=9,
        default=StatusChoices.READY,
        choices=StatusChoices.choices,
        db_index=True,
    )
    is_paid_ok = models.BooleanField(default=False, db_index=True)
