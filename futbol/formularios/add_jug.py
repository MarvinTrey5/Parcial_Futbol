from django import forms
from futbol.models import Equipos

# Tabla de jugadores
class Add_jugad(forms.Form):
    nombre=forms.CharField(max_length=100)
    apellido=forms.CharField(max_length=100)
    nacionalidad=forms.CharField(max_length=100)
    fecha_nacimiento=forms.DateField()
    pertenece_id=forms.ModelChoiceField(queryset=Equipos.objects.all(),empty_label=None, to_field_name="id")