from django.db import models

class Tag(models.Model):
    name = models.CharField(max_length=80, blank=False, verbose_name="Nome")
    slug = models.CharField(max_length=20, blank=False, verbose_name="Slug")
    last_modified = models.DateTimeField(auto_now=True)
