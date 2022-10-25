from email.policy import default
from enum import unique
from tabnanny import verbose
from django.db import models
from django.conf import settings
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, AbstractUser



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


class Post(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='posts')
	timestamp =  models.DateTimeField(default=timezone.now)
	content = models.TextField()

	class Meta:
		ordering = ['-timestamp']

	def __str__(self):
		return f'{self.user.username}: {self.content}'


class Relationship(models.Model):
	from_user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='relationships', on_delete=models.CASCADE)
	to_user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='related_to', on_delete=models.CASCADE)

	def __str__(self):
		return f'{self.from_user} to {self.to_user}'

	class Meta:
		indexes = [
		models.Index(fields=['from_user', 'to_user',]),
		]


class Paciente(AbstractUser):
	idPaciente= models.AutoField(primary_key=True)
	nombre = models.CharField(max_length=20)
	ApellidoPaterno = models.CharField(max_length=20)
	ApellidoMaterno = models.CharField(max_length=20)
	FechaNacimiento = models.DateField(null=True)
	peso = models.FloatField(null=True)
	altura = models.FloatField(null=True)
	telefono = models.BigIntegerField(null=True)
	correo = models.EmailField(max_length=40, null=True, unique=True)

	USERNAME_FIELD = 'correo'
	REQUIRED_FIELDS = ['username']
	class Meta:
		verbose_name_plural ="Pacientes"

	def __str__(self):
		return f'{self.idPaciente,self.nombre, self.ApellidoPaterno, self.ApellidoMaterno, self.FechaNacimiento, self.peso, self.altura, self.telefono, self.correo}'

	def create_user(self, nombre, password=None):
		"""
		Creates and saves a User with the given email and password.
		"""
		user = self.model(
		nombre=self.save(nombre),
		)

		user.set_password(password)
		user.save(using=self._db)
		return user

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
class Especialidades(models.Model):
	idEspecialidades = models.IntegerField(primary_key=True)
	Nombre = models.CharField(max_length=30)

	def __str__(self):
		return f'{self.Nombre}'

	class Meta:
		verbose_name_plural = 'Especialidades'


class Especialistas(models.Model):
	idEspecialista = models.IntegerField(primary_key=True)
	nombre = models.CharField(max_length=20)
	ApellidoPaterno = models.CharField(max_length=20)
	ApellidoMaterno= models.CharField(max_length=20)
	cedulaMedica = models.IntegerField()
	cedulaEspecialidad = models.IntegerField()
	idEspecialidad = models.ForeignKey(Especialidades, on_delete=models.CASCADE,related_name='hola')
	password = models.CharField(max_length=20,null=False)

	def __str__(self):
		return f'{self.nombre, self.ApellidoPaterno, self.ApellidoMaterno, self.cedulaMedica, self.cedulaEspecialidad}'

	class Meta:
		verbose_name_plural = "Especialistas"
class Horarios (models.Model):
	id = models.IntegerField(primary_key=True)
	dia = models.CharField(max_length=15)
	hora = models.TimeField()
	idEspecialista = models.ForeignKey(Especialistas, on_delete=models.CASCADE,null=True,related_name='hola2')

	def __str__(self):
		return f'{self.dia, self.hora}'

	class Meta:
		verbose_name_plural = "Horarios"
class Estudios(models.Model):
	idEstudios = models.IntegerField(primary_key=True)
	nombre = models.CharField(max_length=20)
	precio = models.FloatField(max_length=6)
	requisitos = models.CharField(max_length=300)
	tiempoAplicacion = models.CharField(max_length=300)
	analiza = models.CharField(max_length=300)

	def __str__(self):
		return f'{self.nombre, self.precio, self.requisitos, self.tiempoAplicacion, self.analiza}'

	class Meta:
		verbose_name_plural = "Estudios"

class Peso(models.Model):
	idPeso = models.IntegerField(primary_key=True)
	peso = models.FloatField()
	idPaciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, related_name='hola3')

	def __str__(self):
		return f'{self.peso}'
		
	class Meta:
		verbose_name_plural = "Peso"
class Consultas(models.Model):
	idConsultas = models.AutoField(primary_key=True)
	motivo = models.CharField(max_length=300)
	fecha = models.DateField()
	nombre = models.CharField(max_length=100, default='Nombre')
	edad = models.IntegerField(default=0)
	peso = models.FloatField(default=0)
	altura = models.FloatField()

	def __str__(self):
		return f'{self.motivo,self.fecha, self.nombre, self.edad, self.peso,self.altura}'
	class Meta:
		verbose_name_plural = "Consultas"
class Altura(models.Model):
	idAltura = models.IntegerField(primary_key=True)
	altura = models.FloatField()
	idPaciente = models.ForeignKey(Paciente, on_delete=models.CASCADE,related_name='hola4')
	
	def __str__(self):
		return f'{self.altura}'

	class Meta:
	  verbose_name_plural = "Altura"
	  

class Laboratorio(models.Model):
	idLaboratorio = models.IntegerField(primary_key=True)
	idMuestra = models.IntegerField()
	idPaciente = models.ForeignKey(Paciente, on_delete=models.CASCADE,related_name='hola5')
	idEstudio = models.ForeignKey(Estudios, on_delete=models.CASCADE,related_name='hola6')

	def __str__(self):
		return f'{self.idMuestra}'


	class Meta:
		verbose_name_plural = "Laboratorio"
class Citas(models.Model):
	idCitas = models.IntegerField(primary_key=True)
	fecha = models.DateField()
	idEspecialista = models.ForeignKey(Especialistas, on_delete=models.CASCADE,related_name='hola7')
	idPaciente = models.ForeignKey(Paciente, on_delete=models.CASCADE,related_name='hola8')

	def __str__(self):
		return f'{self.fecha}'

	class Meta:
		verbose_name_plural = "Citas"
class Resultados_Lab(models.Model):
	idResultados = models.IntegerField(primary_key=True)
	NombreEstudio = models.CharField(max_length=30)
	idPaciente = models.ForeignKey(Paciente,on_delete=models.CASCADE, related_name='hola9')

	def __str__(self):
		return f'{self.NombreEstudio}'

	class Meta:
		verbose_name_plural = 'ResultadosDeLaboratorio'

