from tabnanny import verbose
from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone



class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	image = models.ImageField(default='batman.png')

	def __str__(self):
		return f'Perfil de {self.user.username}'

	def following(self):
		user_ids = Relationship.objects.filter(from_user=self.user)\
								.values_list('to_user_id', flat=True)
		return User.objects.filter(id__in=user_ids)

	def followers(self):
		user_ids = Relationship.objects.filter(to_user=self.user)\
								.values_list('from_user_id', flat=True)
		return User.objects.filter(id__in=user_ids)


class Post(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
	timestamp =  models.DateTimeField(default=timezone.now)
	content = models.TextField()

	class Meta:
		ordering = ['-timestamp']

	def __str__(self):
		return f'{self.user.username}: {self.content}'


class Relationship(models.Model):
	from_user = models.ForeignKey(User, related_name='relationships', on_delete=models.CASCADE)
	to_user = models.ForeignKey(User, related_name='related_to', on_delete=models.CASCADE)

	def __str__(self):
		return f'{self.from_user} to {self.to_user}'

	class Meta:
		indexes = [
		models.Index(fields=['from_user', 'to_user',]),
		]


class Paciente(models.Model):
	idPaciente= models.IntegerField(primary_key=True)
	nombre = models.CharField(max_length=20)
	ApellidoPaterno = models.CharField(max_length=20)
	ApellidoMaterno = models.CharField(max_length=20)
	FechaNacimiento = models.DateField()
	peso = models.FloatField()
	altura = models.IntegerField()
	telefono = models.IntegerField()
	correo = models.EmailField(max_length=40)
	contrasena = models.CharField(max_length=15)

	def __str__(self):
		return f'{self.nombre, self.ApellidoPaterno, self.ApellidoMaterno, self.FechaNacimiento, self.peso, self.altura, self.telefono, self.correo, self.contrasena}'

	class Meta:
		verbose_name_plural ="Pacientes"
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
	idEspecialidad = models.ForeignKey(Especialidades, on_delete=models.CASCADE)

	def __str__(self):
		return f'{self.nombre, self.ApellidoPaterno, self.ApellidoMaterno, self.cedulaMedica, self.cedulaEspecialidad}'

	class Meta:
		verbose_name_plural = "Especialistas"
class Horarios (models.Model):
	id = models.IntegerField(primary_key=True)
	dia = models.CharField(max_length=15)
	hora = models.TimeField()
	idEspecialista = models.ForeignKey(Especialistas, on_delete=models.CASCADE,null=True)

	def __str__(self):
		return f'{self.dia, self.hora}'

	class Meta:
		verbose_name_plural = "Horarios"
class Estudios(models.Model):
	idEstudios = models.IntegerField(primary_key=True)
	nombre = models.CharField(max_length=20)
	precio = models.FloatField(max_length=6)
	requisitos = models.TextField(max_length=300)

	def __str__(self):
		return f'{self.nombre, self.precio, self.requisitos}'

	class Meta:
		verbose_name_plural = "Estudios"

class Peso(models.Model):
	idPeso = models.IntegerField(primary_key=True)
	peso = models.FloatField()
	idPaciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, related_name='+')

	def __str__(self):
		return f'{self.peso}'
		
	class Meta:
		verbose_name_plural = "Peso"
class Consultas(models.Model):
	idConsultas = models.IntegerField(primary_key=True)
	motivo = models.TextField(max_length=300)
	fecha = models.DateTimeField()

	def __str__(self):
		return f'{self.motivo,self.fecha}'
	class Meta:
		verbose_name_plural = "Consultas"
class Altura(models.Model):
	idAltura = models.IntegerField(primary_key=True)
	altura = models.FloatField()
	idPaciente = models.ForeignKey(Paciente, on_delete=models.CASCADE,related_name='+')
	
	def __str__(self):
		return f'{self.altura}'

	class Meta:
	  verbose_name_plural = "Altura"
	  

class Laboratorio(models.Model):
	idLaboratorio = models.IntegerField(primary_key=True)
	idMuestra = models.IntegerField()
	idPaciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
	idEstudio = models.ForeignKey(Estudios, on_delete=models.CASCADE)

	def __str__(self):
		return f'{self.idMuestra}'


	class Meta:
		verbose_name_plural = "Laboratorio"
class Citas(models.Model):
	idCitas = models.IntegerField(primary_key=True)
	fecha = models.DateField()
	idEspecialista = models.ForeignKey(Especialistas, on_delete=models.CASCADE)
	idPaciente = models.ForeignKey(Paciente, on_delete=models.CASCADE,related_name='+')

	def __str__(self):
		return f'{self.fecha}'

	class Meta:
		verbose_name_plural = "Citas"
class Resultados_Lab(models.Model):
	idResultados = models.IntegerField(primary_key=True)
	NombreEstudio = models.CharField(max_length=30)
	idPaciente = models.ForeignKey(Paciente,on_delete=models.CASCADE, related_name='+')

	def __str__(self):
		return f'{self.NombreEstudio}'

	class Meta:
		verbose_name_plural = 'ResultadosDeLaboratorio'

