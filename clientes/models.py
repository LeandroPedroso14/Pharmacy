from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=50)
    sobrenome = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    nome = models.CharField(max_length=12)

    def __str__(self) -> str:
        return self.nome

        
