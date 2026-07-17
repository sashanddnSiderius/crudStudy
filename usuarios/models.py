from django.db import models

# Create your models here.
class Usuario(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=50, unique=True, null=False, blank=False)
    cpf = models.CharField(max_length=11,unique=True, null=False, blank=False)
    endereco= models.CharField(max_length=100, null=False, blank=False)
    data_nascimento = models.DateField(null=False, blank=False)

def __str__(self):
        return self.name