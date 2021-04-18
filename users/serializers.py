from rest_framework import serializers
from .models import Usuario

class UsuarioSerializer(serializers.ModelSerializer):

    class Meta:
        model = Usuario
        fields = ('first_name', 'last_name', 'password', 'username')
