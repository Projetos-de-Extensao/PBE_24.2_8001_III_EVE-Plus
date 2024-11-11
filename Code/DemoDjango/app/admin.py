from django.contrib import admin
from .models import Employee,Department #importa o employee e department de models

# Register your models here.

# Adiciona o model employee no server 
admin.site.register(Employee)
admin.site.register(Department)