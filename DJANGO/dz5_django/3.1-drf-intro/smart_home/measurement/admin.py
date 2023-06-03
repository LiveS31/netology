from django.contrib import admin

# Register your models here.
from .models import Sensor, Measurement

@admin.register(Sensor) # регистрируем Sensor
class SenorAdmin(admin.ModelAdmin):
    pass

@admin.register(Measurement) # регистрируем Measurement
class Measurement(admin.ModelAdmin):
    pass