from django.db import models

# Create your models here.

class Script(models.Model):
    code        = models.TextField(blank=True, null=True)
    user        = models.TextField(blank=True, null=True)