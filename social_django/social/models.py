from email.policy import default
from enum import unique
from tabnanny import verbose
from django.db import models
from django.conf import settings
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, AbstractUser, UserManager
from .widget import DatePickerInput
from django.core.validators import RegexValidator
from datetime import *



class Profile(models.Model):
	user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	image = models.ImageField(default='batman.png')

	def __str__(self):
		return f'Perfil de {self.user.username}'

	def following(self):
		user_ids = Relationship.objects.filter(from_user=self.user)\
								.values_list('to_user_id', flat=True)
		return settings.AUTH_USER_MODEL.objects.filter(id__in=user_ids)

	def followers(self):
		user_ids = Relationship.objects.filter(to_user=self.user)\
								.values_list('from_user_id', flat=True)
		return settings.AUTH_USER_MODEL.objects.filter(id__in=user_ids)


class Relationship(models.Model):
	from_user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='relationships', on_delete=models.CASCADE)
	to_user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='related_to', on_delete=models.CASCADE)

	def __str__(self):
		return f'{self.from_user} to {self.to_user}'

	class Meta:
		indexes = [
		models.Index(fields=['from_user', 'to_user',]),
		]

class Especialidades(models.Model):
	idEspecialidades = models.AutoField(primary_key=True)
	nombre = models.CharField(max_length=30)

	def __str__(self):
		return f'{self.nombre}'

	class Meta:
		verbose_name_plural = 'Especialidades'
class Paciente(AbstractUser):
	idPaciente= models.AutoField(primary_key=True)
	nombre = models.CharField(max_length=20,null=False)
	ApellidoPaterno = models.CharField(max_length=20,null=False)
	ApellidoMaterno = models.CharField(max_length=20,null=False)
	FechaNacimiento = models.DateField(null=True)
	peso = models.PositiveIntegerField(validators=[RegexValidator(r'^\d{1,10}$')],null=True)
	altura = models.PositiveIntegerField(validators=[RegexValidator(r'^\d{1,10}$')],null=True)
	correo = models.EmailField(max_length=40, unique=True,default='example@email.com',null=False)
	contrasena=models.CharField(max_length=128, default='hola',null=False)
	telefono = models.CharField(max_length=10,validators=[RegexValidator(r'^\d{1,10}$')],null=False, default='0')
	cedulaMedica = models.CharField(max_length=10,validators=[RegexValidator(r'^\d{1,10}$')],null=True)
	cedulaEspecialidad = models.CharField(max_length=10,validators=[RegexValidator(r'^\d{1,10}$')],null=True)
	idEspecialidad = models.ForeignKey(Especialidades, on_delete=models.CASCADE,related_name='id',unique=False,null=True)
	is_active = models.BooleanField(default=True)
	is_superuser = models.BooleanField(default=False)
	is_especialista = models.BooleanField(default=False)
	is_paciente = models.BooleanField(default=False)
	especialidad = models.CharField(max_length=100,null=True)

	USERNAME_FIELD = 'correo'
	REQUIRED_FIELDS = ['username']
	class Meta:
		verbose_name_plural ="Pacientes"

	def __str__(self):
		return f'{self.nombre, self.ApellidoPaterno, self.ApellidoMaterno}'

	def create_superuser(self, nombre, password):
		"""
		Creates and saves a superuser with the given email and password.
		"""
		user = self.create_user(
		nombre,
		password=password,
		)
		user.staff = True
		user.admin = True
		user.save(using=self._db)
		return user
	
	@property
	def edad(self):
		if(self.FechaNacimiento != None):
			edad = date.today().year - self.FechaNacimiento.year
			return edad

class Especialistas(AbstractBaseUser):
	idEspecialista = models.AutoField(primary_key=True)
	nombre = models.CharField(max_length=20)
	ApellidoPaterno = models.CharField(max_length=20)
	ApellidoMaterno= models.CharField(max_length=20)
	correo = models.EmailField(max_length=40, unique=True,default='example@email.com')
	telefono = models.CharField(max_length=10,null=True,validators=[RegexValidator(r'^\d{1,10}$')])
	USERNAME_FIELD = 'correo'
	REQUIRED_FIELDS = ['username']

	def __str__(self):
		return f'{self.nombre, self.correo}'
	
	objects = UserManager()

	class Meta:
		verbose_name_plural = "Especialistas"
class Horarios (models.Model):
	id = models.AutoField(primary_key=True)
	dia = models.CharField(max_length=15)
	horas = models.CharField(max_length=150, default='+')
	especialista = models.CharField(max_length=60,null=False, default="Especialista")

	def __str__(self):
		return f'{self.horas}'

	class Meta:
		verbose_name_plural = "Horarios"
class Estudios(models.Model):
	idEstudios = models.AutoField(primary_key=True)
	nombre = models.CharField(max_length=20, null=True)
	precio = models.FloatField(max_length=6, null=True)
	requisitos = models.CharField(max_length=300, null=True)
	tiempoAplicacion = models.CharField(max_length=300, null=True)
	analiza = models.CharField(max_length=300, null=True)

	def __str__(self):
		return f'{self.nombre}'

	class Meta:
		verbose_name_plural = "Estudios"

class Peso(models.Model):
	idPeso = models.AutoField(primary_key=True)
	peso = models.FloatField()
	idPaciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, related_name='hola3')

	def __str__(self):
		return f'{self.peso}'
		
	class Meta:
		verbose_name_plural = "Peso"
class Consultas(models.Model):
	idConsultas = models.AutoField(primary_key=True)
	motivo = models.CharField(max_length=300)
	fecha = models.DateField(null=True)
	nombre = models.CharField(max_length=100, default='Nombre')
	edad = models.PositiveIntegerField(default=0)
	peso = models.PositiveIntegerField(validators=[RegexValidator(r'^\d{1,10}$')],null=True)
	altura = models.PositiveIntegerField(validators=[RegexValidator(r'^\d{1,10}$')],null=True)
	doctor = models.TextField(max_length=100, default='Doctor')

	def __str__(self):
		return f'{self.idConsultas,self.motivo,self.fecha, self.nombre, self.edad, self.peso,self.altura, self.doctor}'
	class Meta:
		verbose_name = 'consultas'
		verbose_name_plural = 'consultas'

class Altura(models.Model):
	idAltura = models.AutoField(primary_key=True)
	altura = models.FloatField()
	idPaciente = models.ForeignKey(Paciente, on_delete=models.CASCADE,related_name='hola4')
	
	def __str__(self):
		return f'{self.altura}'

	class Meta:
	  verbose_name_plural = "Altura"
	  
class Laboratorio(models.Model):
	idLaboratorio = models.AutoField(primary_key=True)
	Muestra = models.CharField(max_length=5)
	Paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE,related_name='+')
	Estudio = models.ForeignKey(Estudios, on_delete=models.CASCADE,related_name='+')

	def __str__(self):
		return f'{self.Muestra}'

	class Meta:
		verbose_name_plural = "Laboratorio"

class ResultadosLab(models.Model):
	idResultados = models.AutoField(primary_key=True)
	Paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE,related_name='+')
	Muestra = models.CharField(max_length=5)
	GlobulosRojos = models.IntegerField(null=True)
	GlobulosBlancos = models.IntegerField(null=True)
	Colesterol = models.IntegerField(null=True)
	Glucosa = models.IntegerField(null=True)
	TSH = models.IntegerField(null=True)
	Trigliceridos = models.IntegerField(null=True)

	def __str__(self):
		return f'{self.idResultados}'

	class Meta:
		verbose_name_plural = "Resultados"		

class Citas(models.Model):
	idCitas = models.AutoField(primary_key=True)
	fecha = models.DateField()
	especialista = models.ForeignKey(Especialistas, on_delete=models.CASCADE,related_name='hola7')
	paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE,related_name='hola8')
	hora = models.TimeField(blank=True,null=True)

	def __str__(self):
		return f'{self.fecha}'

	class Meta:
		verbose_name_plural = "Citas"
class Resultados_Lab(models.Model):
	idResultados = models.AutoField(primary_key=True)
	NombreEstudio = models.CharField(max_length=30)
	idPaciente = models.ForeignKey(Paciente,on_delete=models.CASCADE, related_name='hola9')

	def __str__(self):
		return f'{self.NombreEstudio}'

	class Meta:
		verbose_name_plural = 'ResultadosDeLaboratorio'

class RolesUsuarios(models.Model):
	idTipo = models.AutoField(primary_key=True)
	nombre = models.CharField(max_length=30)
	rol = models.CharField(max_length=1)

	def __str__(self):
		return f'{self.rol,self.nombre}'
	
	class Meta:
		verbose_name_plural = 'Roles'

class login(models.Model):
	idlogin = models.AutoField(primary_key=True)
	username = models.CharField(max_length=63)
	password = models.CharField(max_length=63)
	
	def __str__(self):
		return f'{self.username,self.password}'
	
	class Meta:
		verbose_name_plural = 'Login'

class Hacercitas(models.Model):
	especialidad = models.CharField(max_length=100, null=True)
	dia=models.IntegerField(null=True)
	hora=models.IntegerField(default=0,null=True)
	especialista=models.CharField(max_length=100)

	def __str__(self):
		return f'{self.dia,self.hora,self.especialista}'