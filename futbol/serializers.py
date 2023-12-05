from rest_framework import serializers
from .models import Equipos,Jugadores,Noticias

class FrameSerialiazer(serializers.ModelSerializer):
    class Meta:
        model=Equipos
        fields = ["id","nombre","ciudad","pais","titulos","fundado"]

class FrameSerialiazer1(serializers.ModelSerializer):
    class Meta:
        model=Jugadores
        fields = ["id","nombre","apellido","nacionalidad","fecha_nacimiento","pertenece_id"]

class FrameSerialiazer2(serializers.ModelSerializer):
    class Meta:
        model=Noticias
        fields = ["id","resultado","encuentros","analisis"]
