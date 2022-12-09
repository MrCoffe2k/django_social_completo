from cProfile import label
from dataclasses import fields
from pyexpat import model
from django import forms
from django.forms import *
from django.contrib.auth.forms import *
from .models import *
from .widget import *
from django.contrib.auth.hashers import *
from django.core.validators import *

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

class Consulta(forms.ModelForm):
	motivo = forms.CharField(label="Observaciones",widget=forms.Textarea(attrs={'rows':10, 'placeholder':'Observaciones'}), required=True)
	fecha = forms.DateField(label="Fecha",widget=DatePickerInput)
	nombre = forms.CharField(label="Nombre del paciente", max_length=100,widget=forms.Textarea(attrs={'rows':1, 'placeholder':'Nombre del paciente'}))
	peso = forms.FloatField(label="Peso",widget=forms.NumberInput(attrs={'rows':1, 'placeholder':'Peso (Kg)'}))
	altura = forms.FloatField(label="Altura", widget=forms.NumberInput(attrs={'rows':1, 'placeholder':'Altura(cm)'}))
	edad = forms.IntegerField(label = "Edad", widget=forms.NumberInput(attrs={'rows':1, 'placeholder':'Edad'}))
	doctor = forms.ModelChoiceField(
    queryset=Paciente.objects.filter(is_especialista=True),label='Doctor',widget=forms.Select(attrs={'class': 'choice'}))

	class Meta:
		model= Consultas
		fields=['fecha','doctor','nombre','edad','peso','altura','motivo']
		help_texts = {k:"" for k in fields}

class Catalogo(forms.ModelForm):
	nombre= forms.CharField(label="Nombre del estudio")
	precio = forms.FloatField(label="Precio")
	tiempoAplicacion = forms.CharField(label="Tiempo de Aplicacion")
	analiza = forms.CharField(label="¿Que analiza?")
	requisitos = forms.CharField(label="Requisitos", widget=forms.Textarea(attrs={'rows':10, 'placeholder':'Requisitos'}), required=True)
	class Meta:
		model= Estudios
		fields=['nombre','precio','tiempoAplicacion','analiza','requisitos']

class Catalogo2(forms.ModelForm):
	nombre= forms.CharField(label="Nombre del estudio", disabled=True)
	precio = forms.FloatField(label="Precio", disabled=True)
	tiempoAplicacion = forms.CharField(label="Tiempo de Aplicacion", disabled=True)
	analiza = forms.CharField(label="¿Que analiza?", disabled=True)
	requisitos = forms.CharField(label="Requisitos", widget=forms.Textarea(attrs={'rows':10, 'placeholder':'Requisitos'}), disabled=True)
	class Meta:
		model= Estudios
		fields=['nombre','precio','tiempoAplicacion','analiza','requisitos']

class busquedalaboratorios(forms.ModelForm):
	nombre = forms.ModelChoiceField(queryset=Estudios.objects.filter(precio__gt = 1 ), empty_label=None, widget=forms.Select(attrs={'class':'choice'}))

	class Meta:
		model= Estudios
		fields = ['nombre']
class EspecialidadesForm(forms.ModelForm):
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
	Estudio= forms.ModelChoiceField(queryset=Estudios.objects.filter(precio__gt = 1 ),label='Estudios',widget=forms.Select(attrs={'class':'choice'}))
	Paciente = forms.ModelChoiceField(queryset=Paciente.objects.filter(is_paciente=True),label='Paciente', widget=forms.Select(attrs={'class':'choice'}))
	Muestra = forms.CharField(label="Numero de muestra",max_length=10,validators=[RegexValidator(r'^\d{1,10}$')],required=True)
	class Meta:
		model= Laboratorio
		fields=['Estudio','Paciente','Muestra']

class Resultadoslab(forms.ModelForm):
	Paciente = forms.ModelChoiceField(queryset=Paciente.objects.filter(is_paciente=True),label='Paciente', widget=forms.Select(attrs={'class':'choice'}))
	Muestra = forms.ModelChoiceField(queryset=Laboratorio.objects.all(),label='Número de muestra', widget=forms.Select(attrs={'class':'choice'}))
	GlobulosRojos = forms.CharField(label="Niveles de globulos rojos",max_length=3,validators=[RegexValidator(r'^\d{1,10}$')],required=True)
	GlobulosBlancos = forms.CharField(label="Niveles de globulos blancos",max_length=3,validators=[RegexValidator(r'^\d{1,10}$')],required=True)
	Colesterol = forms.CharField(label="Niveles de colesterol total",max_length=3,validators=[RegexValidator(r'^\d{1,10}$')],required=True)
	Glucosa = forms.CharField(label="Niveles de glucosa",max_length=3,validators=[RegexValidator(r'^\d{1,10}$')],required=True)
	TSH = forms.CharField(label="Niveles de TSH (hormona estimulante de la tiroides)",max_length=3,validators=[RegexValidator(r'^\d{1,10}$')],required=True)
	Trigliceridos = forms.CharField(label="Niveles de trigliceridos",max_length=3,validators=[RegexValidator(r'^\d{1,10}$')],required=True)
	class Meta:
		model= ResultadosLab
		fields=['Paciente','Muestra','GlobulosRojos','GlobulosBlancos','Colesterol','Glucosa','TSH','Trigliceridos']
		
class Horarios(forms.ModelForm):
	DIAS = (
			(1,'Lunes'),
			(2,'Martes'),
			(3,'Miercoles'),
			(4,'Jueves'),
			(5,'Viernes'),
			(6,'Sabado'),
			(7,'Domingo'),
		)
	dia =  forms.ChoiceField(choices=DIAS, widget=forms.Select(attrs={'class':'choice'}))
	horaInicio = forms.TimeField(widget=TimePickerInput)
	horaFinal = forms.TimeField(widget=TimePickerInput)
	especialista = forms.ModelChoiceField(
		queryset=Paciente.objects.filter(is_especialista=True),label='Doctor', widget=forms.Select(attrs={'class':'choice'}))
	class Meta:
			model= Horarios
			fields=['especialista','dia','horaInicio','horaFinal']

class Citas(forms.ModelForm):
	especialista = forms.ModelChoiceField(
    queryset=Paciente.objects.filter(is_especialista=True),label='Doctor',widget=forms.Select)
	class Meta:
		model= Hacercitas
		fields=['especialista']


class Citas2(forms.ModelForm):
	DIAS = (
			(1,'Lunes'),
			(2,'Martes'),
			(3,'Miercoles'),
			(4,'Jueves'),
			(5,'Viernes'),
			(6,'Sabado'),
			(7,'Domingo'),
		)
	dia= forms.ChoiceField(choices=DIAS)
	class Meta:
		model= Hacercitas
		fields=['dia']

class Citas3(forms.ModelForm):
	hora=forms.TimeField(widget=TimePickerInput)
	class Meta:
		model= Hacercitas
		fields=['hora']



