from django.db                    import models
from django.contrib.auth.models   import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.contrib.auth.hashers  import make_password


class UserManager(BaseUserManager):
    def create_user(self, username, password=None):
        if not username:
            raise ValueError ('El usuario debe tener un Username')
        user = self.model(username=username)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, username2, password2):
        user = self.create_user(
            username=username2,
            password=password2                        
        )
        user.is_admin = True
        user.save(using=self._db)
        return user
class User (AbstractBaseUser, PermissionsMixin):
    id              = models.IntegerField('id_persona', primary_key=True, unique=True)
    username        = models.CharField('username', max_length=20, unique=True)
    password        = models.CharField('contrasena', max_length=256)
    name            = models.CharField ('nombre', max_length=50)
    email           = models.EmailField ('email', max_length=100)
    type_user       = models.CharField('tipo_usuario', max_length=30)
    
    
    def save (self, **kwargs):
        some_salt = 'mMUj0DrIK6vgtdIYepkIxN'
        self.password = make_password (self.password, some_salt)
        super().save(**kwargs)
        
    objects = UserManager()
    USERNAME_FIELD ='username'