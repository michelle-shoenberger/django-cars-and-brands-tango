from django.contrib import admin

from .models import Brand, Car

# Register your models here.
admin.site.register(Car)
admin.site.register(Brand)