from django.db import models
# from django.core.validators import MinLengthValidator
from projects.models import Project


class ImportData(models.Model):
    last_modified = models.DateTimeField(auto_now=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
