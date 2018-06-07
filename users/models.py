# from django.db import models
from django.contrib.auth.models import User

# Create your models here.]


def set_email_as_unique():
    """
    Sets the email field as unique=True in auth.User Model
    """
    email_field = dict([(field.name, field) for
                       field in User._meta.fields])["email"]
    setattr(email_field, '_unique', True)

# this is called here so that attribute can be set at the application load time


set_email_as_unique()
