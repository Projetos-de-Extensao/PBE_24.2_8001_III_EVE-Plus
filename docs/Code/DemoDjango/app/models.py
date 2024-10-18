from django.db import models

# Create your models here.

#1. python .\manage.py makemigrations --> verifica se possui algum novo model e gera novo migrations
#2. python .\manage.py migrate --> gera a tabela a partir das classes detectadas pelo comando acima

# Feito em aula --> 18/10/24
class Department(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    role = models.CharField(max_length=100)
    department = models.ForeignKey(Department,on_delete=models.CASCADE)

    def __str__(self):
        return self.name



