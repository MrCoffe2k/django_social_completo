from django.contrib import admin
from .models import Horarios,Altura, Citas, Consultas, Especialidades, Especialistas, Estudios, Laboratorio, Paciente, Peso, Post, Profile, Relationship, Resultados_Lab

# Register your models here.
admin.site.register(Profile)
admin.site.register(Post)
admin.site.register(Relationship)
admin.site.register(Horarios)
admin.site.register(Paciente)
admin.site.register(Resultados_Lab)
admin.site.register(Especialidades)
admin.site.register(Especialistas)
admin.site.register(Estudios)
admin.site.register(Peso)
admin.site.register(Consultas)
admin.site.register(Altura)
admin.site.register(Laboratorio)
admin.site.register(Citas)


