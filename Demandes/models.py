from django.db import models
from Auth.models import *
# Create your models here.

class Demande(models.Model):
    patient    = models.ForeignKey(Patient, on_delete=models.CASCADE)
    medecine    = models.ForeignKey(Medecine, on_delete=models.CASCADE)
    resultat = models.BooleanField(null=True)
    def __str__(self):
        return str(self.patient) +' demande '+str(self.medecine)