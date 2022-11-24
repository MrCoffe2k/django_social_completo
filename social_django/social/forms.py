from cProfile import label
from dataclasses import fields
from pyexpat import model
from django import forms
from django.forms import *
from django.contrib.auth.forms import *
from .models import *
from .widget import *
from django.contrib.auth.hashers import *
from django.core.validators import RegexValidator

class UserRegisterForm(UserCreationForm):
	nombre = forms.CharField(label='Nombre',max_length=20,required=True)
	ApellidoPaterno = forms.CharField(label='Apellido Paterno',max_length=20,required=True)
	ApellidoMaterno = forms.CharField(label='Apellido Materno',max_length=20,required=True)
	FechaNacimiento = forms.DateField(label='Fecha', widget=DatePickerInput, required=True)
	peso = forms.CharField(label='Peso',max_length=3,validators=[RegexValidator(r'^\d{1,10}$')],required=True)
	altura = forms.CharField(label='Altura',max_length=3,validators=[RegexValidator(r'^\d{1,10}$')],required=True)
	telefono = forms.CharField(label='Telefono',max_length=10,validators=[RegexValidator(r'^\d{1,10}$')],required=True)
	correo = forms.EmailField(label='Correo',max_length=40,required=True)
	password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput,required=True)
	password2 = forms.CharField(label='Confirmar Contraseña', widget=forms.PasswordInput,required=True)
	is_paciente = forms.BooleanField(label='¿Aceptas terminos y condiciones?',initial=False,required=True)
	
	class Meta:
		model = Paciente
		fields =['nombre','ApellidoPaterno','ApellidoMaterno','FechaNacimiento','peso','altura','telefono','correo','password1','password2','is_paciente']
		help_texts = {k:"" for k in fields}

class StaffRegisterForm(UserCreationForm):
	nombre = forms.CharField(label='Nombre',max_length=20,required=True)
	ApellidoPaterno = forms.CharField(label='Apellido Paterno',max_length=20,required=True)
	ApellidoMaterno = forms.CharField(label='Apellido Materno',max_length=20,required=True)
	FechaNacimiento = forms.DateField(label='Fecha', widget=DatePickerInput, required=True)
	telefono = forms.CharField(label='Telefono',max_length=10,validators=[RegexValidator(r'^\d{1,10}$')])
	cedulaMedica = forms.CharField(label='Cedula Medica',max_length=10,validators=[RegexValidator(r'^\d{1,10}$')],required=True)
	cedulaEspecialidad = forms.CharField(label='Cedula Especialidad',max_length=10,validators=[RegexValidator(r'^\d{1,10}$')],required=True)
	correo = forms.EmailField(label='Correo',max_length=40,required=True)
	password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput,required=True)
	password2 = forms.CharField(label='Confirmar Contraseña', widget=forms.PasswordInput,required=True)
	is_especialista = forms.BooleanField(label='¿Aceptas terminos y condiciones?',initial=False,required=True)
	
	class Meta:
		model = Paciente
		fields =['nombre','ApellidoPaterno','ApellidoMaterno','FechaNacimiento','cedulaMedica','cedulaEspecialidad','telefono','correo','password1','password2','is_especialista']
		help_texts = {k:"" for k in fields}

class PacienteForm(forms.ModelForm):
	nombre = forms.CharField(label='Nombre',max_length=20,required=True)
	ApellidoPaterno = forms.CharField(label='Apellido Paterno',max_length=20,required=True)
	ApellidoMaterno = forms.CharField(label='Apellido Materno',max_length=20,required=True)
	FechaNacimiento = forms.DateField(label='Fecha de nacimiento', disabled=True)
	peso = forms.CharField(label='Peso',max_length=3,validators=[RegexValidator(r'^\d{1,10}$')],required=True)
	altura = forms.CharField(label='Altura',max_length=3,validators=[RegexValidator(r'^\d{1,10}$')],required=True)
	telefono = forms.CharField(label='Telefono',max_length=10,validators=[RegexValidator(r'^\d{1,10}$')],required=True)
	correo = forms.EmailField(label='Correo',max_length=40,required=True)
	password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput(render_value=True, attrs={'placeholder': '••••••••••••••••••••••••'}),required=False)
	password2 = forms.CharField(label='Confirmar Contraseña', widget=forms.PasswordInput(render_value=True, attrs={'placeholder': '••••••••••••••••••••••••'}),required=False)

	class Meta:
		model = Paciente
		fields =['nombre','ApellidoPaterno','ApellidoMaterno','FechaNacimiento','peso','altura','telefono','correo','password1','password2']
		help_texts = {k:"" for k in fields}

class StaffForm(forms.ModelForm):
	nombre = forms.CharField(label='Nombre',max_length=20,required=True)
	ApellidoPaterno = forms.CharField(label='Apellido Paterno',max_length=20,required=True)
	ApellidoMaterno = forms.CharField(label='Apellido Materno',max_length=20,required=True)
	FechaNacimiento = forms.DateField(label='Fecha de nacimiento', disabled=True)
	telefono = forms.CharField(label='Telefono',max_length=10,validators=[RegexValidator(r'^\d{1,10}$')],required=True)
	cedulaMedica = forms.CharField(label='Cedula Medica',max_length=10,validators=[RegexValidator(r'^\d{1,10}$')],required=True)
	cedulaEspecialidad = forms.CharField(label='Cedula Especialidad',max_length=10,validators=[RegexValidator(r'^\d{1,10}$')],required=True)
	correo = forms.EmailField(label='Correo',max_length=40,required=True)
	password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput(render_value=True, attrs={'placeholder': '••••••••••••••••••••••••'}),required=False)
	password2 = forms.CharField(label='Confirmar Contraseña', widget=forms.PasswordInput(render_value=True, attrs={'placeholder': '••••••••••••••••••••••••'}),required=False)

	class Meta:
		model = Paciente
		fields =['nombre','ApellidoPaterno','ApellidoMaterno','FechaNacimiento','telefono','cedulaMedica','cedulaEspecialidad','correo','password1','password2']
		help_texts = {k:"" for k in fields}

class PostForm(forms.ModelForm):
	content = forms.CharField(label='', widget=forms.Textarea(attrs={'rows':2, 'placeholder': '¿Qué está pasando?'}), required=True)

	class Meta:
		model = Post
		fields = ['content']

class Consulta(forms.ModelForm):
	motivo = forms.CharField(label="Observaciones",widget=forms.Textarea(attrs={'rows':10, 'placeholder': 'Observaciones'}), required=True)
	fecha = forms.DateField(label="Fecha",widget=DatePickerInput)
	nombre = forms.CharField(label="Nombre del paciente", max_length=100,widget=forms.Textarea(attrs={'rows':1, 'placeholder': 'Nombre del paciente'}))
	peso = forms.FloatField(label="Peso",widget=forms.NumberInput(attrs={'rows':1, 'placeholder': 'Peso (Kg)'}))
	altura = forms.FloatField(label="Altura", widget=forms.NumberInput(attrs={'rows':1, 'placeholder': 'Altura(cm)'}))
	edad = forms.IntegerField(label = "Edad", widget=forms.NumberInput(attrs={'rows':1, 'placeholder': 'Edad'}))
	doctor = forms.ModelChoiceField(
    queryset=Paciente.objects.filter(is_especialista=True),label='Doctor',widget=forms.Select)

	class Meta:
		model= Consultas
		fields=['fecha','doctor','nombre','edad','peso','altura','motivo']

		widgets = {
            'fecha' : DatePickerInput(),
        }

class Catalogo(forms.ModelForm):
	nombre= forms.CharField(label="Nombre del estudio")
	precio = forms.FloatField(label="Precio")
	tiempoAplicacion = forms.CharField(label="Tiempo de Aplicacion")
	analiza = forms.CharField(label="¿Que analiza?")
	requisitos = forms.CharField(label="Requisitos", widget=forms.Textarea(attrs={'rows':10, 'placeholder': 'Requisitos'}), required=True)
	class Meta:
		model= Estudios
		fields=['nombre','precio','tiempoAplicacion','analiza','requisitos']


class busquedalaboratorios(forms.ModelForm):
	opciones = forms.ModelChoiceField(queryset=Estudios.objects.all(), empty_label=None)

	class Meta:
		model= Estudios
		fields = '__all__'
class Especialidades:
	nombre = forms.CharField(label='Nombre')

	class Meta:
		model = Especialidades
		fields =['nombre']

class LoginForm(forms.ModelForm):
	username = forms.CharField(label="Correo")
	password = forms.CharField(widget=forms.PasswordInput, label="Contraseña")		

	class Meta:
		model = Paciente
		fields = ['username', 'password']

class LoginForm2(forms.ModelForm):
	username = forms.CharField(label="Usuario")
	password = forms.CharField(widget=forms.PasswordInput, label="Contraseña")		

	class Meta:
		model = Especialistas
		fields = ['username', 'password']

class Laboratorios(forms.ModelForm):
	Estudio= forms.ModelChoiceField(
    queryset=Estudios.objects.all(),label='Estudios',widget=forms.Select)
	Muestra = forms.FloatField(label="Numero de muestra")
	Paciente = forms.ModelChoiceField(
    queryset=Paciente.objects.filter(is_paciente=True),label='Paciente',widget=forms.Select)
	class Meta:
		model= Laboratorio
		fields=['Estudio','Muestra']

