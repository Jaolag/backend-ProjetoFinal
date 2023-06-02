from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Tarefa(models.Model):
    titulo = models.CharField(max_length=50)
    descricao = models.CharField(max_length=1000)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)