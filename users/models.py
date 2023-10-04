from django.db import models
from django.contrib.auth.models import User


class Confirm(models.Model):
    code = models.IntegerField()
    user = models.OneToOneField(User, on_delete=models.CASCADE)
