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


class Paciente(AbstractBaseUser):
	objects = BaseUserManager()
	idPaciente= models.IntegerField(primary_key=True)
	nombre = models.CharField(max_length=20, unique=True,default="Nombre")
	ApellidoPaterno = models.CharField(max_length=20)
	ApellidoMaterno = models.CharField(max_length=20)
	FechaNacimiento = models.DateField()
	peso = models.FloatField()
	altura = models.FloatField()
	telefono = models.BigIntegerField()
	correo = models.EmailField(max_length=40)

	USERNAME_FIELD = 'nombre'

	def __str__(self):
		return f'{self.nombre, self.ApellidoPaterno, self.ApellidoMaterno, self.FechaNacimiento, self.peso, self.altura, self.telefono, self.correo}'

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
	requisitos = models.TextField(max_length=300)

	def __str__(self):
		return f'{self.nombre, self.precio, self.requisitos}'

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

	class User(AbstractUser):
		
		email = models.EmailField(('email address'),unique=True,)
	is_active = models.BooleanField(default=True)
	staff = models.BooleanField(default=False) # a admin user; non super-user
	admin = models.BooleanField(default=False) # a superuser
	

	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = [] # Email & Password are required by default.

	def get_full_name(self):
	# The user is identified by their email address
		return self.email

	def get_short_name(self):
	# The user is identified by their email address
		return self.email

	def __str__(self):
		return self.email

	def has_perm(self, perm, obj=None):
		"Does the user have a specific permission?"
	# Simplest possible answer: Yes, always
		return True

	def has_module_perms(self, app_label):
		"Does the user have permissions to view the app `app_label`?"
	# Simplest possible answer: Yes, always
		return True

	@property
	def is_staff(self):
		"Is the user a member of staff?"
		return self.staff

	@property
	def is_admin(self):
		"Is the user a admin member?"
		return self.admin


class UserManager(BaseUserManager):
	def create_user(self, email, password=None):
		"""
	Creates and saves a User with the given email and password.
	"""
		if not email:
			raise ValueError('Users must have an email address')
		user = self.model(
		email=self.normalize_email(email),
		)

		user.set_password(password)
		user.save(using=self._db)
		return user

	def create_staffuser(self, email, password):
		"""
		Creates and saves a staff user with the given email and password.
		"""
		user = self.create_user(
		email,
		password=password,
		)
		user.staff = True
		user.save(using=self._db)
		return user

	def create_superuser(self, email, password):
		"""
		Creates and saves a superuser with the given email and password.
		"""
		user = self.create_user(
		email,
		password=password,
		)
		user.staff = True
		user.admin = True
		user.save(using=self._db)
		return user

	# hook in the New Manager to our Model