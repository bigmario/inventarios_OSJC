# Generated by Django 2.2 on 2021-02-07 20:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Alumno',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('ci', models.CharField(max_length=50, unique=True)),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('telf', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('nucleo', models.CharField(max_length=50)),
            ],
            options={
                'ordering': ['apellido'],
            },
        ),
        migrations.CreateModel(
            name='Representante',
            fields=[
                ('ci', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('telf', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254, unique=True)),
            ],
            options={
                'ordering': ['apellido'],
            },
        ),
        migrations.CreateModel(
            name='Instrumento',
            fields=[
                ('serial', models.CharField(max_length=1000, primary_key=True, serialize=False)),
                ('sin_fundamusical', models.CharField(max_length=100, unique=True)),
                ('nombre', models.CharField(max_length=50)),
                ('marca', models.CharField(max_length=50)),
                ('modelo', models.CharField(max_length=50)),
                ('familia', models.CharField(choices=[('CUE', 'Cuerdas'), ('VMA', 'Viento-Madera'), ('VME', 'Viento_Metal'), ('PER', 'Percusion')], max_length=13)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['nombre'],
            },
        ),
        migrations.CreateModel(
            name='Comodato',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('fecha', models.DateTimeField(default=django.utils.timezone.now)),
                ('alumno', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='inventario.Alumno')),
                ('instrumento_serial', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='inventario.Instrumento')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['fecha'],
            },
        ),
        migrations.AddField(
            model_name='alumno',
            name='representante_id',
            field=models.ForeignKey(db_constraint=False, on_delete=django.db.models.deletion.CASCADE, to='inventario.Representante'),
        ),
    ]
