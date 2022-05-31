from django.shortcuts import get_object_or_404, render
from rest_framework.views import APIView
from rest_framework.response import Response
from Demandes.models import Demande
from rest_framework.generics import (ListAPIView,ListCreateAPIView)
from rest_framework import generics
from Demandes.serializers import DemandeSerializer
# Create your views here.
class PatientDemande(APIView):
    def post(self, request, *args, **kwargs):
       
        serializer = DemandeSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        response = Response()
        response.data = {
            "message":"Demmande created successfully"
        }
        return response
    def patch(self, request, *args, **kwargs):
        id= request.data['id']
        demande = Demande.objects.get(id=id)
        data = request.data
        demande.id = data.get("id", demande.id)
        demande.resultat = data.get("resultat", demande.resultat)
        demande.save()
        serializer = DemandeSerializer(demande)

        return Response(serializer.data)
class DemandesDefineAll(ListCreateAPIView):
        queryset =Demande.objects.all()
        serializer_class =DemandeSerializer
        pagination_class = None
        Demande.objects  


class DemandeRetrieve(ListAPIView):
    serializer_class =DemandeSerializer
    def get_queryset(self):
        return Demande.objects.filter(id=self.kwargs.get('pk', None)) 

class DemandeRemove(APIView):
   def delete(self, request, *args, **kwargs):
        demande= Demande.objects.filter(id=self.kwargs.get('pk', None)) 
        demande.delete()
        return Response({'message': 'Demande was deleted successfully!'})



class DemandeRetrievemed(ListAPIView):
    serializer_class =DemandeSerializer
    def get_queryset(self):
        return Demande.objects.filter(medecine=self.kwargs.get('pk', None)) 


class DemandeReponse(APIView):
   def patch(self, request, *args, **kwargs):
        id= request.data['id']
        demande = Demande.objects.get(id=id)
        data = request.data
        demande.id = data.get("id", demande.id)
        demande.resultat = data.get("resultat", demande.resultat)
        demande.save()
        serializer = DemandeSerializer(demande)
        return Response(serializer.data)

