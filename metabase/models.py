from django.db import models
from django.contrib.auth.models import User
from dashboards.models import Dashboard


class Iframe(models.Model):
    name = models.CharField(max_length=80, blank=False, verbose_name="Nome")
    user = models.ForeignKey(User, limit_choices_to={'is_staff': True},
                             on_delete=models.CASCADE)
    dashboard = models.ForeignKey(Dashboard, on_delete=models.CASCADE)
    uuid = models.CharField(max_length=32, blank=False)
