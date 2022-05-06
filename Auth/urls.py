from django.urls import path


from .views import (
MedecineLoginView,
MedecineSignupView,
PatientLoginView,
PatientSignupView)

urlpatterns=[
    path('signup/medecine/', MedecineSignupView.as_view()),
    path('signup/patient/', PatientSignupView.as_view()),
    path('login/patient/', PatientLoginView.as_view()),
    path('login/medecine/', MedecineLoginView.as_view()),


]