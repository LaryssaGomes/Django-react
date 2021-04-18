from django.shortcuts import render
from .serializers import *
from .models import Usuario
# rest_framework
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from django.http import HttpResponse
# Create your views here.

@api_view(['GET', 'POST'])
def usuarios(request):

    if request.method == 'GET':
        data = Usuario.objects.all()
        serializer = UsuarioSerializer(data, context={'request': request} ,many=True)
        return Response({'data': serializer.data})

    elif request.method == 'POST':
        serializer = UsuarioSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        