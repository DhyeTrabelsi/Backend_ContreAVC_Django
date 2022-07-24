from rest_framework import serializers
from Auth.models import Adminstrateur, User,Medecine,Patient


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=[]

class AdminstrateurSerializer(serializers.ModelSerializer):
    class Meta:
        model=Adminstrateur
        fields=['username','password']
        extra_kwargs={
            'password':{'write_only':True}
        }
    
    def save(self, **kwargs):
        user=Adminstrateur(
            username=self.validated_data['username'],
            password=self.validated_data['password']
        )
        user.save()
        return user

class MedecineSerializer(serializers.ModelSerializer):
    class Meta:
        model=Medecine
        fields=['username','email','password','first_name','last_name','telephone','postion']
        extra_kwargs={
            'password':{'write_only':True}
        }
    
    def save(self, **kwargs):
        medecine=Medecine(
            username=self.validated_data['username'],
            email=self.validated_data['email'],
            password=self.validated_data['password'],
            last_name=self.validated_data['last_name'],
            first_name=self.validated_data['first_name'],
            telephone=self.validated_data['telephone'],
            postion=self.validated_data['postion'],

        )
        medecine.save()
        return medecine

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model=Patient
        fields=['username','email','password','firstname','lastname','telephone','birthday','gender','poids','postion','medecine',
        'avg_glucose_level','bmi','ever_married','smoking_status','stroke','hypertension','heart_disease','type_de_travail','notifier']       
        extra_kwargs={
            'password':{'write_only':True}
        }
    
    def save(self, **kwargs):
        patient=Patient(
            username=self.validated_data['username'],
            email=self.validated_data['email'],
            password=self.validated_data['password'],
            lastname=self.validated_data['lastname'],
            firstname=self.validated_data['firstname'],
            telephone=self.validated_data['telephone'],
            birthday=self.validated_data['birthday'],
            gender=self.validated_data['gender'],
            postion=self.validated_data['postion'],
            poids=self.validated_data['poids'],
            medecine=self.validated_data['medecine'],
            avg_glucose_level=self.validated_data['avg_glucose_level'],
            bmi=self.validated_data['bmi'],
            ever_married=self.validated_data['ever_married'],
            smoking_status=self.validated_data['smoking_status'],
            type_de_travail=self.validated_data['type_de_travail'],
            heart_disease=self.validated_data['heart_disease'],
            hypertension=self.validated_data['hypertension'],
            stroke=self.validated_data['stroke'],
            notifier=self.validated_data['notifier'],

          

            )

        patient.save()
        return patient
