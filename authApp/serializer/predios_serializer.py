from authApp.models.predios import Predios
from rest_framework           import serializers

class PredioSerializer (serializers.ModelSerializer):
    class Meta:
        model = Predios
        field= ['id_predio', 'cedula_catastral','tipo_predio', 'direccion']