from django.contrib import admin
from .models import Adminstrateur, Medecine, Patient
# Register your models here.

admin.site.register(Medecine)
admin.site.register(Patient)
admin.site.register(Adminstrateur)

