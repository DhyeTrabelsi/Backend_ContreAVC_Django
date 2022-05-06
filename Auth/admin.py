from django.contrib import admin
from .models import Medecine, Patient, User
# Register your models here.

admin.site.register(Medecine)
admin.site.register(Patient)
admin.site.register(User)