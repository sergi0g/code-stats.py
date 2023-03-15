from django.db import models
from django.core.validators import MinLengthValidator
import secrets

# Create your models here.

def generate():
    return secrets.token_hex(32)

class Machine(models.Model):
    user = models.CharField(max_length=20)
    name = models.CharField(max_length=20)
    token = models.CharField(max_length=64, default=generate, validators=[MinLengthValidator(64, '64 characters required')])

    def __str__(self):
        return self.name

class XPEntry(models.Model):
    user = models.CharField(max_length=20)
    date = models.DateTimeField()
    language = models.CharField(max_length=32)
    xp = models.IntegerField(default=0)
    machine = models.CharField(max_length=20)