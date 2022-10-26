# Generated by Django 3.1.2 on 2022-10-26 00:18

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('idPaciente', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=20)),
                ('ApellidoPaterno', models.CharField(max_length=20)),
                ('ApellidoMaterno', models.CharField(max_length=20)),
                ('FechaNacimiento', models.DateField(null=True)),
                ('peso', models.FloatField(null=True)),
                ('altura', models.FloatField(null=True)),
                ('telefono', models.BigIntegerField(null=True)),
                ('correo', models.EmailField(max_length=40, null=True, unique=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name_plural': 'Pacientes',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Consultas',
            fields=[
                ('idConsultas', models.AutoField(primary_key=True, serialize=False)),
                ('motivo', models.CharField(max_length=300)),
                ('fecha', models.DateField()),
                ('nombre', models.CharField(default='Nombre', max_length=100)),
                ('edad', models.IntegerField(default=0)),
                ('peso', models.FloatField(default=0)),
                ('altura', models.FloatField()),
            ],
            options={
                'verbose_name_plural': 'Consultas',
            },
        ),
        migrations.CreateModel(
            name='Especialidades',
            fields=[
                ('idEspecialidades', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=30)),
            ],
            options={
                'verbose_name_plural': 'Especialidades',
            },
        ),
        migrations.CreateModel(
            name='Especialistas',
            fields=[
                ('idEspecialista', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=20)),
                ('ApellidoPaterno', models.CharField(max_length=20)),
                ('ApellidoMaterno', models.CharField(max_length=20)),
                ('cedulaMedica', models.IntegerField()),
                ('cedulaEspecialidad', models.IntegerField()),
                ('password', models.CharField(max_length=20)),
                ('idEspecialidad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hola', to='social.especialidades')),
            ],
            options={
                'verbose_name_plural': 'Especialistas',
            },
        ),
        migrations.CreateModel(
            name='Estudios',
            fields=[
                ('idEstudios', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=20)),
                ('precio', models.FloatField(max_length=6)),
                ('requisitos', models.CharField(max_length=300)),
                ('tiempoAplicacion', models.CharField(max_length=300)),
                ('analiza', models.CharField(max_length=300)),
            ],
            options={
                'verbose_name_plural': 'Estudios',
            },
        ),
        migrations.CreateModel(
            name='Resultados_Lab',
            fields=[
                ('idResultados', models.AutoField(primary_key=True, serialize=False)),
                ('NombreEstudio', models.CharField(max_length=30)),
                ('idPaciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hola9', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'ResultadosDeLaboratorio',
            },
        ),
        migrations.CreateModel(
            name='Relationship',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('from_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='relationships', to=settings.AUTH_USER_MODEL)),
                ('to_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='related_to', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='batman.png', upload_to='')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now)),
                ('content', models.TextField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-timestamp'],
            },
        ),
        migrations.CreateModel(
            name='Peso',
            fields=[
                ('idPeso', models.AutoField(primary_key=True, serialize=False)),
                ('peso', models.FloatField()),
                ('idPaciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hola3', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Peso',
            },
        ),
        migrations.CreateModel(
            name='Laboratorio',
            fields=[
                ('idLaboratorio', models.AutoField(primary_key=True, serialize=False)),
                ('idMuestra', models.IntegerField()),
                ('idEstudio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hola6', to='social.estudios')),
                ('idPaciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hola5', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Laboratorio',
            },
        ),
        migrations.CreateModel(
            name='Horarios',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('dia', models.CharField(max_length=15)),
                ('hora', models.TimeField()),
                ('idEspecialista', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='hola2', to='social.especialistas')),
            ],
            options={
                'verbose_name_plural': 'Horarios',
            },
        ),
        migrations.CreateModel(
            name='Citas',
            fields=[
                ('idCitas', models.AutoField(primary_key=True, serialize=False)),
                ('fecha', models.DateField()),
                ('idEspecialista', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hola7', to='social.especialistas')),
                ('idPaciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hola8', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Citas',
            },
        ),
        migrations.CreateModel(
            name='Altura',
            fields=[
                ('idAltura', models.AutoField(primary_key=True, serialize=False)),
                ('altura', models.FloatField()),
                ('idPaciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hola4', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Altura',
            },
        ),
        migrations.AddIndex(
            model_name='relationship',
            index=models.Index(fields=['from_user', 'to_user'], name='social_rela_from_us_28f36a_idx'),
        ),
    ]
