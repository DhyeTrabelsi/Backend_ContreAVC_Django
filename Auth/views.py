
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from Auth.models import Adminstrateur, Patient,Medecine
from .serializers import  AdminstrateurSerializer, MedecineSerializer, PatientSerializer
from rest_framework.generics import (ListCreateAPIView)

class MedecineSignupView(generics.GenericAPIView):
    serializer_class=MedecineSerializer
    def post(self, request, *args, **kwargs):
        serializer=self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
            "message":"account created successfully"
        })
class PatientSignupView(generics.GenericAPIView):
    serializer_class=PatientSerializer
    def post(self, request, *args, **kwargs):
        serializer=self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
            "message":"account created successfully"
        })


class AdminstrateurLoginView(APIView):
    def post(self, request):
        login= request.data['username']
        password = request.data['password']

        admin = Adminstrateur.objects.filter(username=login).first()
        if admin is None:
            raise AuthenticationFailed('admin not found!')
        if not (password==admin.password):
            raise AuthenticationFailed('Incorrect password!')
        response = Response()
        admin = Adminstrateur.objects.get(username=login)        
        admin_serializer = AdminstrateurSerializer(admin) 
        response.data = {
            'data':admin_serializer.data
        }
        return response
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
        Patients_serializer = PatientSerializer(patient) 
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
        medecines_serializer = MedecineSerializer(medecine) 
        response.data = {
            'data':medecines_serializer.data
        }
        return response
class PatientDefineAll(ListCreateAPIView):
        queryset =Patient.objects.all()
        serializer_class =PatientSerializer
        pagination_class = None
        Patient.objects       

class MedecineDefineAll(ListCreateAPIView):
        queryset =Medecine.objects.all()
        serializer_class =MedecineSerializer
        pagination_class = None
        Medecine.objects       


class PatientUpdate(APIView):
   def patch(self, request, *args, **kwargs):
        username= request.data['username']
        patient = Patient.objects.get(username=username)
        data = request.data
        patient.stroke = data.get("email", patient.email)
        patient.stroke = data.get("password", patient.password)
        patient.stroke = data.get("lastname", patient.lastname)
        patient.stroke = data.get("firstname", patient.firstname)
        patient.stroke = data.get("telephone", patient.telephone)
        patient.stroke = data.get("avg_glucose_level", patient.avg_glucose_level)
        patient.stroke = data.get("bmi", patient.bmi)
        patient.stroke = data.get("ever_married", patient.ever_married)
        patient.stroke = data.get("smoking_status", patient.smoking_status)
        patient.stroke = data.get("medecine", patient.medecine)        
        patient.stroke = data.get("stroke", patient.stroke)
        patient.save()
        serializer = PatientSerializer(patient)
        return Response(serializer.data)

class MedecineUpdate(APIView):
   def patch(self, request, *args, **kwargs):
        username= request.data['username']
        patient = Medecine.objects.get(username=username)
        data = request.data
        patient.stroke = data.get("email", patient.email)
        patient.stroke = data.get("password", patient.password)
        patient.stroke = data.get("lastname", patient.lastname)
        patient.stroke = data.get("firstname", patient.firstname)
        patient.stroke = data.get("telephone", patient.telephone)
        patient.save()
        serializer = MedecineSerializer(patient)
        return Response(serializer.data)