from django.contrib import admin

# Register your models here.
from .models import Reservation
from .models import Shoes

admin.site.register(Reservation)
admin.site.register(Shoes)