from django import forms
from .models import Vehiculo
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class VehiculoForm(forms.ModelForm):
    class Meta:
        model = Vehiculo
        fields = '__all__'
        
class RegistroUsuarioForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email') 