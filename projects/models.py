from django.db import models

# Create your models here.
class Project(models.Model): #Herdando da model
   
   
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100, blank=True, verbose_name="Nome")
    description = models.TextField(verbose_name="Descrição")