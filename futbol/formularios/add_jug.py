from django import forms

# Tabla de jugadores
class Add_jugad(forms.Form):
    nombre=forms.CharField(max_length=100)
    apellido=forms.CharField(max_length=100)
    nacionalidad=forms.CharField(max_length=100)
    fecha_nacimiento=forms.DateTimeField()
    perteneid=forms.IntegerField()