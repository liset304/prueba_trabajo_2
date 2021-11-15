from django.contrib import admin

# Register your models here.
from .models.user import User
from .models.predios import Predios

admin.site.register(User)
admin.site.register(Predios)