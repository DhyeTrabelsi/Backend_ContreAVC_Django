from .views import *
from django.urls import path



urlpatterns = [

    path('demande/',PatientDemande.as_view() ),
    path('demandes/list/',DemandesDefineAll.as_view() ),
    path('demandes/<str:pk>/',DemandeRetrieve.as_view()), 
    path('demandes/remove/<str:pk>/',DemandeRemove.as_view()), 
    path('demandes/med/<str:pk>/',DemandeRetrievemed.as_view()), 
    path('demande/reponse/',DemandeReponse.as_view() ),



]