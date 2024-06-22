from django.contrib import admin

# Register your models here.
from .models import Reservation, ReservStatus


admin.site.register(Reservation)
admin.site.register(ReservStatus)
