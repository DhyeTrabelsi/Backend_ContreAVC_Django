from Demandes.models import *
from rest_framework import serializers 

class DemandeSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Demande
        fields = [
            'id','patient',
                  'medecine',
                  'resultat'
                  ]
        def save(self, **kwargs):
            demande=Demande(
                patient=self.validated_data['patient'],
                medecine=self.validated_data['medecine'],
                resultat=self.validated_data['resultat'],
        
            )
            demande.save()
            return demande
