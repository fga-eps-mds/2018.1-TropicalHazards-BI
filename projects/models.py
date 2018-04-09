from django.db import models
from django.core.validators import MinLengthValidator
from django.contrib.auth.models import User


# Create your models here.
class Project(models.Model):  # Herdando da model

    name = models.CharField(max_length=80, validators=[MinLengthValidator(5)],
                            blank=False, verbose_name="Nome")
    description = models.TextField(verbose_name="Descrição", max_length=250)
    user = models.ForeignKey(User, limit_choices_to={'is_staff': True},
                             on_delete=models.CASCADE)
