from django.db import models

# Create your models here.
class Films(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField(default=0)
    description = models.TextField()