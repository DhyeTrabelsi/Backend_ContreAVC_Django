
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.views import APIView

from Auth.models import Patient,Medecine
from .serializers import  MedecineSignupSerializer, PatientSignupSerializer

class MedecineSignupView(generics.GenericAPIView):
    serializer_class=MedecineSignupSerializer
    def post(self, request, *args, **kwargs):
        serializer=self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
            "message":"account created successfully"
        })
class PatientSignupView(generics.GenericAPIView):
    serializer_class=PatientSignupSerializer
    def post(self, request, *args, **kwargs):
        serializer=self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
            "message":"account created successfully"
        })

class PatientLoginView(APIView):
    def post(self, request):
        login= request.data['username']
        password = request.data['password']

        patient = Patient.objects.filter(username=login).first()
        if patient is None:
            raise AuthenticationFailed('User not found!')
        if not (password==patient.password):
            raise AuthenticationFailed('Incorrect password!')
        response = Response()
        patient = Patient.objects.get(username=login)        
        Patients_serializer = PatientSignupSerializer(patient) 
        response.data = {
            'data':Patients_serializer.data
        }
        return response
class MedecineLoginView(APIView):
    def post(self, request):
        login= request.data['username']
        password = request.data['password']

        medecine = Medecine.objects.filter(username=login).first()
        if medecine is None:
            raise AuthenticationFailed('User not found!')
        if not (password==medecine.password):
            raise AuthenticationFailed('Incorrect password!')
        response = Response()
        medecine = Medecine.objects.get(username=login)        
        Patients_serializer = PatientSignupSerializer(medecine) 
        response.data = {
            'data':Patients_serializer.data
        }
        return response
