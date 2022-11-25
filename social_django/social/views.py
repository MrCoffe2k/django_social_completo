from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *
from django import forms
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth import login, authenticate
User = get_user_model()

def index(request):
    context = {}
    return render(request, 'social/index.html', context)

User = settings.AUTH_USER_MODEL

def feed(request):
	posts = Post.objects.all()
	context = { 'posts': posts}
	return render(request, 'social/feed.html', context)

def registroPaciente(request):
	if request.method == 'POST':
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data['correo']
			messages.success(request, f'Usuario {username} creado')
			return redirect('login')
	else:
		form = UserRegisterForm()

	context = { 'form' : form }
	return render(request, 'social/register.html', context)

def registroStaff(request):
	if request.method == 'POST':
		form = StaffRegisterForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data['correo']
			messages.success(request, f'Usuario {username} creado')
			return redirect('menu3')
	else:
		form = StaffRegisterForm()

	context = { 'form' : form }
	return render(request, 'social/register.html', context)

def login_page(request):
	form = LoginForm(request.POST or None)
	if request.method == 'POST':
		if form.is_valid():
			username=form.cleaned_data.get('username')
			password=form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None and user.is_especialista and user.is_active:
				login(request, user)
				return redirect('menu')
			elif user is not None and user.is_paciente and user.is_active:
				login(request, user)
				return redirect('menu2')
			elif user is not None and user.is_superuser and user.is_active:
				login(request, user)
				return redirect('menu3')
			else:
				messages.error(request, 'Correo o contraseña incorrectos')
	return render(request, 'social/login.html', context={'form': form})

def gestionarpaciente(request,idPaciente):
	paciente = Paciente.objects.filter(idPaciente = idPaciente).first()
	form = PacienteForm(instance=paciente)
	return render(request, "social/gestionarpaciente.html", {"form":form})

def actualizarpaciente(request, idPaciente):
	paciente = Paciente.objects.get(pk=idPaciente)
	form = PacienteForm(request.POST, instance=paciente)
	if form.is_valid():
		form.save()
	return render(request, "social/feed.html", {"paciente":paciente})

def gestionarstaff(request,idPaciente):
	paciente = Paciente.objects.filter(idPaciente = idPaciente).first()
	form = StaffForm(instance=paciente)
	return render(request, "social/gestionarstaff.html", {"form":form})

def actualizarstaff(request, idPaciente):
	paciente = Paciente.objects.get(pk=idPaciente)
	form = StaffForm(request.POST, instance=paciente)
	if form.is_valid():
		form.save()
	return render(request, "social/feed.html", {"paciente":paciente})

def eliminarcuenta(request):
    user_pk = request.user.pk
    User = get_user_model()
    User.objects.filter(pk=user_pk).update(is_active=False)
    messages.success(request, 'Perfil eliminado')
    return redirect('login')

def creacionconsulta(request):
	if request.method == 'POST':
		form = Consulta(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request, f'Consulta creada')
			return redirect('creacionconsulta')
	else:
		form = Consulta()

	context = { 'form' : form }
	return render(request, "social/creacionconsulta.html", context)


def catalogolaboratorios(request):
	if request.method == 'POST':
		form = Catalogo(request.POST)
		if form.is_valid():
			form.save()
			return redirect('feed')
	else:
		form = Catalogo()

	context = { 'form' : form }
	return render(request, "social/catalogolaboratorios.html", context)


def busquedalaboratorios(request):
	context = {}
	return render(request, "social/busquedalaboratorios.html")
	
def menu(request):
	context = {}
	return render(request, 'social/menu.html')

def menu2(request):
	context = {}
	return render(request, 'social/menu2.html')

def menu3(request):
	context = {}
	return render(request, 'social/menu3.html')

def citas(request):
	context = {}
	return render(request, 'social/citas.html')

def establecerhorarios(request):
	context = {}
	return render(request, 'social/establecerhorarios.html')
	
def creacionexpediente(request):
	posts = Consultas.objects.all()
	context = { 'Consulta': Consultas}
	return render(request, 'social/creacionexpediente.html', context)

def expediente(request):
	if request.method == "POST":
		busqueda = request.POST['busqueda']
		consultas = Consultas.objects.filter(nombre__contains=busqueda)
		return render(request,'social/expediente.html', {'busqueda':busqueda}, {'consultas':consultas})
	else:
		return render(request,'social/expediente.html')

def busquedaexpediente(request):
	context = {}
	return render(request, 'social/busquedaexpediente.html')
	
def asignarlaboratorio(request):
	context = {}
	return render(request, 'social/asignarlaboratorio.html')

def visualizacionderesultados(request):
	context = {}
	return render(request, 'social/visualizacionderesultados.html')

def staff(request):
	return render(request,'social/menu.html')

def paciente(request):
	return render(request,'social/menu2.html')