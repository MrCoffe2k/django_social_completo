from cProfile import label
from dataclasses import fields
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Paciente, Post

class UserRegisterForm(UserCreationForm):
	nombre = forms.CharField(label='Nombre',max_length=20)
	ApellidoPaterno = forms.CharField(label='Apellido Paterno',max_length=20)
	ApellidoMaterno = forms.CharField(label='Apellido Materno',max_length=20)
	FechaNacimiento = forms.DateField(label='Fecha de Nacimiento (Año-Mes-Dia)')
	peso = forms.FloatField(label='Peso (Kg)')
	altura = forms.FloatField(label='Altura (cm)',)
	telefono = forms.IntegerField(label='Telefono',)
	correo = forms.EmailField(label='Correo',max_length=40)
	password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
	password2 = forms.CharField(label='Confirmar Contraseña', widget=forms.PasswordInput)


	class Meta:
		model = Paciente
		fields =['nombre','ApellidoPaterno','ApellidoMaterno','FechaNacimiento','peso','altura','telefono','correo','password1','password2']
		help_texts = {k:"" for k in fields}

class PostForm(forms.ModelForm):
	content = forms.CharField(label='', widget=forms.Textarea(attrs={'rows':2, 'placeholder': '¿Qué está pasando?'}), required=True)

	class Meta:
		model = Post
		fields = ['content']
