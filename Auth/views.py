
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from Auth.models import Adminstrateur, Patient,Medecine
from .serializers import  AdminstrateurSerializer, MedecineSerializer, PatientSerializer
from rest_framework.generics import (ListCreateAPIView,RetrieveUpdateAPIView)

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

class PatientDefineMed(ListCreateAPIView):
      serializer_class =PatientSerializer
      def get_queryset(self):
            return Patient.objects.filter(medecine=self.kwargs.get('pk', None))      

class PatientNotifier(APIView):
   def patch(self, request, *args, **kwargs):
        username= request.data['username']
        patient = Patient.objects.get(username=username)
        data = request.data
     
        patient.username = data.get("username", patient.username)
        patient.notifier = data.get("notifier", patient.notifier)
        patient.save()
        serializer = PatientSerializer(patient)
        return Response(serializer.data)


class PatientUpdate(APIView):
   def patch(self, request, *args, **kwargs):
        username= request.data['username']
        patient = Patient.objects.get(username=username)
        data = request.data
     

        patient.username = data.get("username", patient.username)
        patient.email = data.get("email", patient.email)
        patient.password = data.get("password", patient.password)
        patient.lastname = data.get("lastname", patient.lastname)
        patient.firstname = data.get("firstname", patient.firstname)
        patient.telephone = data.get("telephone", patient.telephone)
        patient.postion = data.get("postion", patient.postion)

        patient.ever_married = data.get("ever_married", patient.ever_married)
        patient.type_de_travail = data.get("type_de_travail", patient.type_de_travail)

        patient.save()
        serializer = PatientSerializer(patient)
        return Response(serializer.data)

class PatientReponse(APIView):
   def patch(self, request, *args, **kwargs):
        username= request.data['username']
        medecine= request.data['medecine']
        patient = Patient.objects.get(username=username)
        data = request.data
        patient.username = data.get("username", patient.username)
        patient.medecine =  Medecine.objects.get(username=medecine)
        patient.save()
        serializer = PatientSerializer(patient)
        return Response(serializer.data)

class MedecineUpdate(APIView):
   def patch(self, request, *args, **kwargs):
        username= request.data['username']
        medecine = Medecine.objects.get(username=username)
        data = request.data
        
        medecine.username = data.get("username", medecine.username)
        medecine.email = data.get("email", medecine.email)
        medecine.password = data.get("password", medecine.password)
        medecine.last_name = data.get("last_name", medecine.last_name)
        medecine.first_name = data.get("first_name", medecine.first_name)
        medecine.postion = data.get("postion", medecine.postion)
        medecine.telephone = data.get("telephone", medecine.telephone)
        medecine.save()
        serializer = MedecineSerializer(medecine)

        return Response(serializer.data)

class MedecineDelete(APIView):
   def delete(self, request, *args, **kwargs):
        medecine=Medecine.objects.filter(username=self.kwargs.get('pk', None)) 
        medecine.delete() 
        return Response({'message': 'Medecine was deleted successfully!'})

class PatientDelete(APIView):
   def delete(self, request, *args, **kwargs):
        patient=Patient.objects.filter(username=self.kwargs.get('pk', None)) 
        patient.delete() 
        return Response({'message': 'Patient was deleted successfully!'})