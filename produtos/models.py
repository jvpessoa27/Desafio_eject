from datetime import datetime
from django.db import models
from usuario.models import Usuario

produto = (
    ('eletronico', 'Eletrônico'),
    ('televisao', 'Televisão'),
    ('computador', 'Computador'),
    ('celular', 'Celular'),
    ('audio e video', 'Áudio e Vídeo'),

)

class Produto(models.Model):
    nome = models.CharField(verbose_name='Nome do produto', max_length=200)
    email = models.CharField(verbose_name='Email para contato', max_length=50)
    preco = models.IntegerField()
    foto_produto = models.ImageField(upload_to='fotos/%d/%m/%y/')
    descricao = models.TextField()
    data_produto = models.DateTimeField(default=datetime.now)
    categoria = models.CharField(verbose_name='Categoria', max_length=20, choices=produto, default='eletronico')
    usuario = models.ForeignKey(
        Usuario,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
