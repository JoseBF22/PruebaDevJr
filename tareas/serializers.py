from rest_framework import serializers
from .models import Tarea, Autor, Libro

class TareaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tarea
        fields = '__all__'

class AutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Autor
        fields = '__all__'

class LibroSerializer(serializers.ModelSerializer):
    autor = AutorSerializer()

    class Meta:
        model = Libro
        fields = '__all__'