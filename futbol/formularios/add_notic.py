from django import forms
# Tabla de noticias
class Add_notic(forms.Form):
    resultado=forms.CharField(max_length=50)
    encuentros=forms.CharField(max_length=100)
    analisis=forms.CharField(max_length=100)