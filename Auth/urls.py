from django.urls import path
from rest_framework.authtoken import views


from .views import (
AdminstrateurLoginView,
MedecineDefineAll,
MedecineLoginView,
MedecineSignupView,
PatientDefineAll,
PatientLoginView,
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
    path('update/', PatientUpdate.as_view()),
    path('api-token-auth/', views.obtain_auth_token)


]