# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-11 23:24
from __future__ import unicode_literals

from django.conf import settings
import django.contrib.auth.models
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import enumfields.fields
import re
import user.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0001_initial'),
        ('auth', '0008_alter_user_username_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(max_length=30, unique=True, validators=[django.core.validators.RegexValidator(re.compile('^[\\w.@+-]+$', 32), 'O nome do user so pode conter letras, digitos ou osseguintes caracteres @/./+/-/_invalid')], verbose_name='Nome do Usuário')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='E-mail')),
                ('nome', models.CharField(blank=True, max_length=100, verbose_name='Nome')),
                ('data_de_entrada', models.DateTimeField(auto_now_add=True, verbose_name='Data de entrada')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('tags', models.ManyToManyField(related_name='tags_do_usuario', through='core.Tag_Usuario', to='core.Tag')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'Usuário',
                'verbose_name_plural': 'Usuários',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='CheckinItemInscricao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField(auto_now_add=True, verbose_name='Data de entrada')),
                ('hora', models.TimeField(blank=True, default='00:00', verbose_name='Hora')),
                ('status', enumfields.fields.EnumField(default='NAO_VERIFICADO', enum=user.models.StatusCheckIn, max_length=10)),
                ('gerente', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='gerente_chekin', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Inscricao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status_inscricao', enumfields.fields.EnumField(default='ativa', enum=user.models.StatusInscricao, max_length=10)),
                ('tipo_inscricao', enumfields.fields.EnumField(default='PARCIAL', enum=user.models.TipoInscricao, max_length=10)),
            ],
            options={
                'verbose_name': 'Id de Inscricao',
                'verbose_name_plural': 'Id das Inscricoes',
            },
        ),
        migrations.CreateModel(
            name='ItemInscricao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('atividade', models.ForeignKey(blank=True, default='', on_delete=django.db.models.deletion.CASCADE, to='core.Atividade')),
                ('checkin', models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='user.CheckinItemInscricao')),
                ('inscricao', models.ForeignKey(blank=True, default='', on_delete=django.db.models.deletion.CASCADE, related_name='itens', to='user.Inscricao')),
            ],
        ),
        migrations.AddField(
            model_name='inscricao',
            name='atividades',
            field=models.ManyToManyField(through='user.ItemInscricao', to='core.Atividade'),
        ),
        migrations.AddField(
            model_name='inscricao',
            name='evento',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='core.Evento'),
        ),
        migrations.AddField(
            model_name='inscricao',
            name='trilhas',
            field=models.ManyToManyField(through='core.TrilhaInscricao', to='core.Trilha'),
        ),
        migrations.AddField(
            model_name='inscricao',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='inscricoes', to=settings.AUTH_USER_MODEL, verbose_name='user'),
        ),
    ]