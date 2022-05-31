from django.db import models
from datetime import date
from django.contrib.auth.models import AbstractUser
# Create your models here.
GENDER = (
        ('Male', 'Male'),
        ('Female','Female'),
    )
Smoking = (
        ('ex fumeur', 'ex fumeur'),
        ('Actuellement fumeur','Actuellement fumeur'),
        ('Jamais fumeur','Jamais fumeur'),
        ('Inconnu','Inconnu'),

    )
Marié = (
        ('Oui', 'Oui'),
        ('Non','Non'),
    )
travail = (
        ('gouvernement', 'gouvernement'),
        ('privé','privé'),('indépendant','indépendant'),('Pas encore','Pas encore'),
    )
class User(AbstractUser):
    is_medecine=models.BooleanField(default=False)
    is_patient=models.BooleanField(default=False)
    
class Adminstrateur(models.Model):
    username= models.CharField(max_length=30,primary_key=True, default='')   
    password= models.CharField(max_length=255)
    
    REQUIRED_FIELDS = [username,password]

    def __str__(self):
        return self.username
    
class Medecine(models.Model):
    username= models.CharField(max_length=30,primary_key=True, default='')   
    password= models.CharField(max_length=255)
    first_name=models.CharField(max_length=12, null=True)
    last_name=models.CharField(max_length=100, null=True)
    email   = models.EmailField()
    telephone=models.CharField(max_length=12, null=True)
    postion=models.CharField(max_length=60, null=True, blank=True)

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
    postion=models.CharField(max_length=60, null=True, blank=True)
    birthday = models.DateField(null=False,default=date.today)
    gender = models.CharField(max_length = 6, choices = GENDER, default = 'Male')
    poids=models.FloatField(null=True, blank=True,default=0)

    avg_glucose_level=models.FloatField(null=True, blank=True,default=0)
    hypertension=models.IntegerField(null=True, blank=True,default=0)
    heart_disease=models.FloatField(null=True, blank=True,default=0)
    type_de_travail= models.CharField(max_length = 19, choices = travail, default = 'Pas encore', null=True, blank=True)
    bmi=models.FloatField(null=True, blank=True,default=0)
    ever_married= models.CharField(max_length = 3, choices = Marié, default = 'Non', null=True, blank=True)
    smoking_status=models.CharField(max_length =19 , choices = Smoking, default = 'Inconnu', null=True, blank=True)
    stroke=models.IntegerField(null=True, blank=True,default=0)

    medecine= models.ForeignKey(Medecine, on_delete=models.CASCADE, null=True, blank=True)

    REQUIRED_FIELDS = [username,password,firstname,lastname,email,telephone,gender]

    def __str__(self):
        return self.username
