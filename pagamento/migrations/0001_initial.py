# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-05 15:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import enumfields.fields
import pagamento.enum


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('utils', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cupom',
            fields=[
                ('codigo_do_cupom', models.CharField(max_length=100, verbose_name='cupom')),
                ('porcentagem', models.DecimalField(decimal_places=0, default=0, max_digits=2, verbose_name='porcentagem')),
                ('status', enumfields.fields.EnumField(default='ATIVO', enum=pagamento.enum.StatusCupom, max_length=25)),
                ('tipo', enumfields.fields.EnumField(default='SIMPLES', enum=pagamento.enum.TipoCupom, max_length=25)),
                ('periodo', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='utils.Periodo')),
            ],
            options={
                'verbose_name': 'Cupom',
                'verbose_name_plural': 'Pagamentos',
            },
        ),
        migrations.CreateModel(
            name='Pagamento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', enumfields.fields.EnumField(default='NAO_PAGO', enum=pagamento.enum.StatusPagamento, max_length=10)),
                ('data', models.DateField(auto_now_add=True, verbose_name='Data de entrada')),
                ('hora', models.TimeField(verbose_name='Hora')),
                ('valor_pagamento', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='valor pagamento')),
            ],
        ),
        migrations.CreateModel(
            name='PagamentoCupom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cupom', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='cupom_de_pagamento', to='pagamento.Cupom')),
                ('pagamento', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='pagamento_cupom', to='pagamento.Pagamento')),
            ],
        ),
        migrations.AddField(
            model_name='pagamento',
            name='cupons',
            field=models.ManyToManyField(blank=True, default='', through='pagamento.PagamentoCupom', to='pagamento.Cupom'),
        ),
    ]
