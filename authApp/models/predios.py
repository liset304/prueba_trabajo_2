from django.db import models



class Predios (models.Model):
    id_predio           = models.CharField('matricula_inmobiliaria',primary_key=True, max_length=156, unique=True)
    cedula_catastral    = models.CharField('Cedula_catastral', max_length=156, unique=True)
    tipo_predio         = models.CharField('tipo_predio', max_length= 30 )
    direccion           = models.CharField('dirección', max_length=130)
