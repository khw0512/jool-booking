from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Reservation)
admin.site.register(Shoes)
admin.site.register(Top)
admin.site.register(Bottom)