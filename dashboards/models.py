from django.db import models
from django.core.validators import MinLengthValidator
from projects.models import Project
from django.contrib.auth.models import User


class Dashboard(models.Model):
    name = models.CharField(max_length=80, validators=[MinLengthValidator(5)],
                            blank=False, verbose_name="dashboard_name")
    project = models.ForeignKey(Project, limit_choices_to={'is_staff': True},
                                on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
