from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
	path('', views.login_page, name='feed'),
	path('profile/', views.profile, name='profile'),
	path('profile/<str:username>/', views.profile, name='profile'),
	path('registroPaciente/', views.registroPaciente, name='registroPaciente'),
	path('registroStaff/', views.registroStaff, name='registroStaff'),
	path('login_page/', views.login_page, name='login'),
	path('logout/', LogoutView.as_view(template_name='social/logout.html'), name='logout'),
	path('post/', views.post, name='post'),
	path('follow/<str:username>/', views.follow, name='follow'),
	path('unfollow/<str:username>/', views.unfollow, name='unfollow'),
	path('gestionarpaciente/<int:idPaciente>/', views.gestionarpaciente, name='gestionarpaciente'),
	path('actualizarpaciente/<int:idPaciente>/', views.actualizarpaciente, name='actualizarpaciente'),
	path('gestionarstaff/<int:idPaciente>/', views.gestionarstaff, name='gestionarstaff'),
	path('actualizarstaff/<int:idPaciente>/', views.actualizarstaff, name='actualizarstaff'),
    path('eliminarcuenta/<int:idPaciente>/', views.eliminarcuenta, name='eliminarcuenta'),
    path('menu/', views.menu, name='menu'),
    path('menu2/', views.menu2, name='menu2'),
    path('menu3/', views.menu3, name='menu3'),
    path('citas/', views.citas, name='citas'),
    path('establecerhorarios/', views.establecerhorarios, name='establecerhorarios'),
	path('creacionconsulta/', views.creacionconsulta, name='creacionconsulta'),
	path('catalogolaboratorios/', views.catalogolaboratorios, name='catalogolaboratorios'),
	path('busquedalaboratorios/', views.busquedalaboratorios, name='busquedalaboratorios'),
	path('creacionexpediente/', views.creacionexpediente, name='creacionexpediente'),
	path('edicionexpediente/', views.creacionexpediente, name='edicionexpediente'),
	path('asignarlaboratorio/', views.asignarlaboratorio, name='asignarlaboratorio'),
	path('visualizacionderesultados/', views.visualizacionderesultados, name='visualizacionderesultados'),
	path('busquedaexpediente/', views.busquedaexpediente, name='busquedaexpediente'),
	path('expediente/', views.expediente, name='expediente'),
	
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)