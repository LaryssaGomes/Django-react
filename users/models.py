
#from django.contrib.auth.models import AbstractBaseUser


# from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import AbstractUser
from django.db import models

class Usuario(AbstractUser): # Gerenciador de usuarios a
    bio = models.TextField(blank=True)

