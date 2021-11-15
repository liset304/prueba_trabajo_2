from django.db.models import fields
from authApp.models.user            import User
from authApp.models.predios         import Predios
from rest_framework                 import serializers
from .predios_serializer            import PredioSerializer 

class Userserializer (serializers.ModelSerializer):
    Predios = PredioSerializer()
    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'name','email','type_user','predio']

    def create (self, validate_data):
        tipoData = validate_data.pop('predio')
        userInstance = User.objects.create(**validate_data)
        Predios.objects.create(user=userInstance, **tipoData)
        return userInstance
    
    def to_representation(self, obj):
        user         = User.objects.get(id = obj.id)
        predios       = Predios.objects.get(id=obj.id)
        
        return {
            "id" : user.id,
            "username" : user.username,
            "name" :user.name,
            "mail" :user.mail,
            "tipo_usuario": user.type_user,
            "predio" :{
                "id_predio": predios.id_predio,
                "cedula_catastral": predios.cedula_catastral,
                "tipo_predio":predios.tipo_predio,
                "direccion":predios.direccion,
            }


        }
