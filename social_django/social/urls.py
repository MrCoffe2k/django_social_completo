from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
	path('', views.login_page, name='feed'),
	path('registroPaciente/', views.registroPaciente, name='registroPaciente'),
	path('registroStaff/', views.registroStaff, name='registroStaff'),
	path('login_page/', views.login_page, name='login'),
	path('logout/', LogoutView.as_view(template_name='social/logout.html'), name='logout'),
	path('gestionarpaciente/<int:idPaciente>/', views.gestionarpaciente, name='gestionarpaciente'),
	path('actualizarpaciente/<int:idPaciente>/', views.actualizarpaciente, name='actualizarpaciente'),
	path('gestionarstaff/<int:idPaciente>/', views.gestionarstaff, name='gestionarstaff'),
	path('actualizarstaff/<int:idPaciente>/', views.actualizarstaff, name='actualizarstaff'),
    path('eliminarcuenta/', views.eliminarcuenta, name='eliminarcuenta'),
    path('menu/', views.menu, name='menu'),
    path('menu2/', views.menu2, name='menu2'),
    path('menu3/', views.menu3, name='menu3'),
    path('citas/', views.citas, name='citas'),
    path('establecerhorarios/', views.horariosEspecialistas, name='establecerhorarios'),
	path('creacionconsulta/', views.creacionconsulta, name='creacionconsulta'),
	path('edicionconsulta/<int:idConsultas>/', views.edicionconsulta, name='edicionconsulta'),
	path('actualizarconsulta/<int:idConsultas>/', views.actualizarconsulta, name='actualizarconsulta'),
	path('catalogolaboratorios/', views.catalogolaboratorios, name='catalogolaboratorios'),
	path('listadesplegable/', views.listadesplegable, name='busquedalaboratorios'),
	path('busquedalaboratorios/<str:nombre>/', views.busquedalaboratorio2, name='catalogolaboratorios2'),
	path('mostrarlaboratorio/', views.mostrarlaboratorio, name='mostrarlaboratorio'),
	path('creacionexpediente/', views.creacionexpediente, name='creacionexpediente'),
	path('edicionexpediente/', views.creacionexpediente, name='edicionexpediente'),
	path('asignarlaboratorio/', views.asignarlaboratorio, name='asignarlaboratorio'),
	path('visualizacionderesultados/', views.visualizacionderesultados, name='visualizacionderesultados'),
	path('busquedaexpediente/', views.busquedaexpediente, name='busquedaexpediente'),
	path('registroEspecialidades/', views.registrarEspecialidades, name='registroEspecialidades'),
	path('citas/', views.agendarCitas, name='citas'),
	path('expediente/', views.expediente, name='expediente'),
	
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)