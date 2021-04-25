
#from django.contrib.auth.models import AbstractBaseUser


# from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from stdimage.models import StdImageField
from django.db.models import BooleanField

class UsuarioManager(BaseUserManager):  # Essa é a classe é responsável pela administração dos usuários

    use_in_migrations = True

    """ Essa é classe comum para os dois tipos de usuários (Usuário comum e superUsuário)."""

    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('O e-mail é obrigatório')
        email = self.normalize_email(email)
        user = self.model(email=email, username=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    """ Essa função expecifica as permissões do usuário comum"""

    def create_user(self, email, password=None, **extra_fields):
        # extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):  # Essa função expecifica as permissões do superUsuário
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser precisa ter is_superuser=True')

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser precisa ter is_staff=True')

        return self._create_user(email, password, **extra_fields)

class Usuario(AbstractUser): 
    img = StdImageField('Imagem:', upload_to='imagem_user', blank=True, default=False)
    status_email = BooleanField('Status email', null=False, default=False)
    email = models.EmailField(max_length=254, unique=True)
    
    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = []
    def __str__(self):
        return self.email 

    objects = UsuarioManager()
  
