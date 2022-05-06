from rest_framework import serializers
from Auth.models import User,Medecine,Patient


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=[]

class MedecineSignupSerializer(serializers.ModelSerializer):
    class Meta:
        model=Medecine
        fields=['username','email','password','first_name','last_name','telephone']
        extra_kwargs={
            'password':{'write_only':True}
        }
    
    def save(self, **kwargs):
        user=Medecine(
            username=self.validated_data['username'],
            email=self.validated_data['email'],
            password=self.validated_data['password'],
            last_name=self.validated_data['last_name'],
            first_name=self.validated_data['first_name'],
            telephone=self.validated_data['telephone']

        )
        user.save()
        return user

class PatientSignupSerializer(serializers.ModelSerializer):
    class Meta:
        model=Patient
        fields=['username','email','password','firstname','lastname','telephone','birthday','gender','avg_glucose_level','bmi','ever_married','smoking_status','stroke']       
        extra_kwargs={
            'password':{'write_only':True}
        }
    
    def save(self, **kwargs):
        user=Patient(
            username=self.validated_data['username'],
            email=self.validated_data['email'],
            password=self.validated_data['password'],
            lastname=self.validated_data['lastname'],
            firstname=self.validated_data['firstname'],
            telephone=self.validated_data['telephone'],
            birthday=self.validated_data['birthday'],
            gender=self.validated_data['gender'],
            avg_glucose_level=self.validated_data['avg_glucose_level'],
            bmi=self.validated_data['bmi'],
            ever_married=self.validated_data['ever_married'],
            smoking_status=self.validated_data['smoking_status'],
            stroke=self.validated_data['stroke']

            )

        user.save()
        return user
