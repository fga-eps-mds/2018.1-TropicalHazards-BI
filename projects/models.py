from django.db import models

# Create your models here.
class Project(models.Model): #Herdando da model
   
   
    name = models.CharField(max_length=100, blank=False, verbose_name="Nome")
    description = models.TextField(verbose_name="Descrição")