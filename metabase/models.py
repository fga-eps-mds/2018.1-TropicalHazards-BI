from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from dashboards.models import Dashboard


class Iframe(models.Model):
    name = models.CharField(max_length=80, blank=False, verbose_name="Nome")
    user = models.ForeignKey(User, limit_choices_to={'is_staff': True},
                             on_delete=models.CASCADE)
    dashboard = models.ForeignKey(Dashboard, on_delete=models.CASCADE)
    uuid = models.CharField(max_length=40, blank=True)


class MetabaseSession(models.Model):
    session_id = models.CharField(max_length=40, null=False, blank=False)

    def clean(self):
        validate_only_one_instance(self)


def validate_only_one_instance(obj):
    model = obj.__class__
    if(model.objects.count() > 0 and obj.id != model.objects.get().id):
        raise ValidationError("Can only create 1 %s instance" % model.__name__)
