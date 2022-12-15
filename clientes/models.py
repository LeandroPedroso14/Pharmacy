from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=50)
    sobrenome = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    nome = models.CharField(max_length=12)

    def __str__(self) -> str:
        return self.nome

class Tratamento(models.Model):
    tratamento = models.CharField(max_length=50)
    peso = models.CharField(max_length=50)
    idade = models.IntegerField()
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    medicamentos = models.IntegerField(default=0)
    consulta = models.IntegerField(default=0)
    

def __str__(self) -> str:
    return self.tratamento



