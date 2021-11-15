from authApp.models.propiedades import Propiedades
from rest_framework           import serializers

class PropiedadesSerializer (serializers.ModelSerializer):
    class Meta:
        model = Propiedades
        field= ['id_predio', 'id_propiedad']