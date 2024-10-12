from django.shortcuts import render
from rest_framework import generics
from .models import Tarea
from .serializers import TareaSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

class TareaListCreate(generics.ListCreateAPIView):
    queryset = Tarea.objects.all()
    serializer_class = TareaSerializer

class TareaRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tarea.objects.all()
    serializer_class = TareaSerializer

@api_view(['POST'])
def ordenar_lista(request):
    """
    Recibe una lista de números y devuelve la lista ordenada.
    """
    try:
        numeros = request.data.get('numeros', [])
        if not isinstance(numeros, list):
            return Response({"error": "Se requiere una lista de números"}, status=status.HTTP_400_BAD_REQUEST)
        
        if not all(isinstance(n, (int, float)) for n in numeros):
            return Response({"error": "La lista debe contener solo números"}, status=status.HTTP_400_BAD_REQUEST)

        numeros_ordenados = sorted(numeros)
        
        return Response({"numeros_ordenados": numeros_ordenados}, status=status.HTTP_200_OK)
    
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
@api_view(['POST'])
def contar_palabras(request):
    """
    Recibe un archivo de texto y devuelve la cantidad de palabras que contiene.
    """
    try:
        archivo = request.FILES.get('archivo')
        
        if not archivo:
            return Response({"error": "Se requiere un archivo de texto"}, status=status.HTTP_400_BAD_REQUEST)
        
        contenido = archivo.read().decode('utf-8')
        
        palabras = contenido.split()
        cantidad_palabras = len(palabras)
        
        return Response({"cantidad_palabras": cantidad_palabras}, status=status.HTTP_200_OK)
    
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    