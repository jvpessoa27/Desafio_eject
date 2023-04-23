# Generated by Django 4.2 on 2023-04-22 22:31

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('usuario', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200, verbose_name='Nome do produto')),
                ('email', models.CharField(max_length=50, verbose_name='Email para contato')),
                ('preco', models.IntegerField()),
                ('foto_produto', models.ImageField(upload_to='fotos/%d/%m/%y/')),
                ('descricao', models.TextField()),
                ('data_produto', models.DateTimeField(default=datetime.datetime.now)),
                ('categoria', models.CharField(choices=[('eletronico', 'Eletrônico'), ('televisao', 'Televisão'), ('computador', 'Computador'), ('celular', 'Celular'), ('audio e video', 'Áudio e Vídeo')], default='eletronico', max_length=20, verbose_name='Categoria')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuario.usuario')),
            ],
        ),
    ]
