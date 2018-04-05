from django.db import models

# Create your models here.
class Project(models.Model):
   
   
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100, blank=True, default='')
    description = models.TextField()
   
    class Meta:
        ordering = ('created',)