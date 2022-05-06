from django.db import models
from datetime import date
from django.contrib.auth.models import AbstractUser
# Create your models here.
GENDER = (
        ('M', 'Male'),
        ('F','Female'),
    )
Smoking = (
        ('ex', 'ex fumeur'),
        ('Actuellement','Actuellement fumeur'),
        ('Jamais','Jamais fumeur'),
        ('Inconnu','Inconnu'),

    )
Marié = (
        ('Oui', 'Oui'),
        ('Non','Non'),
    )
class User(AbstractUser):
    is_medecine=models.BooleanField(default=False)
    is_patient=models.BooleanField(default=False)

  

class Medecine(models.Model):
    username= models.CharField(max_length=30,primary_key=True, default='')   
    password= models.CharField(max_length=255)
    first_name=models.CharField(max_length=12, null=True, blank=True)
    last_name=models.CharField(max_length=100, null=True, blank=True)
    email   = models.EmailField()
    telephone=models.CharField(max_length=12, null=True, blank=True)
    REQUIRED_FIELDS = [username,password,first_name,last_name,email,telephone]

    def __str__(self):
        return self.username

class Patient(models.Model):
    username= models.CharField(max_length=30,primary_key=True)   
    password= models.CharField(max_length=255)
    firstname=models.CharField(max_length=20, null=True, blank=True)
    lastname=models.CharField(max_length=20, null=True, blank=True)
    email   = models.EmailField()
    telephone=models.CharField(max_length=12, null=True, blank=True)
    birthday = models.DateField(null=False,default=date.today)
    gender = models.CharField(max_length = 2, choices = GENDER, default = 'M')
    avg_glucose_level=models.FloatField(null=True, blank=True,default=0)
    bmi=models.FloatField(null=True, blank=True,default=0)
    ever_married= models.CharField(max_length = 3, choices = Marié, default = 'Non')
    smoking_status=models.CharField(max_length =12 , choices = Smoking, default = 'Inconnu')
    stroke=models.IntegerField(null=True, blank=True,default=0)
    REQUIRED_FIELDS = [username,password,firstname,lastname,email,telephone,gender]

    def __str__(self):
        return self.username