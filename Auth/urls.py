from django.urls import path
from rest_framework.authtoken import views


from .views import (
AdminstrateurLoginView,
MedecineDefineAll,
MedecineDelete,
MedecineLoginView,
MedecineSignupView,
MedecineUpdate,
PatientDefineAll,
PatientDefineMed,
PatientDelete,
PatientLoginView,
PatientNotifier,
PatientReponse,
PatientSignupView,
PatientUpdate,
)

urlpatterns=[
    path('signup/medecine/', MedecineSignupView.as_view()),
    path('signup/patient/', PatientSignupView.as_view()),
    path('login/admin/', AdminstrateurLoginView.as_view()),
    path('login/patient/', PatientLoginView.as_view()),
    path('login/medecine/', MedecineLoginView.as_view()),
    path('patient/list/', PatientDefineAll.as_view()),
    path('medecine/list/', MedecineDefineAll.as_view()),
    path('patient/listmed/<str:pk>/', PatientDefineMed.as_view()),
    path('update/patient/', PatientUpdate.as_view()),
    path('update/medecine/', MedecineUpdate.as_view()),
    path('reponse/patient/', PatientReponse.as_view()),
    path('delete/medecine/<str:pk>/', MedecineDelete.as_view()),
    path('delete/patient/<str:pk>/', PatientDelete.as_view()),
    path('api-token-auth/', views.obtain_auth_token),
    path('notifier/patient/', PatientNotifier.as_view()),




]