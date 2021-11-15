from django.db                    import models
from .user                         import User
from .predios                      import Predios


class Propiedades (models.Model):
    user       = models.ForeignKey(User, related_name=('id_persona'), on_delete=models.CASCADE)
    id_predio  = models.ForeignKey(Predios, related_name=('matricula_inmobiliaria'), on_delete=models.CASCADE)
    id_propiedad =models.AutoField(primary_key=True,)