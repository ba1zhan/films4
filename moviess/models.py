from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name}"


class Fantasy(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name}"



class Movies(models.Model):
    image = models.ImageField(null=True, blank=True, upload_to='moviess/')
    name = models.CharField(max_length=255)
    description = models.TextField(default='', blank=True)
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True, blank=True
    )
    tags = models.ManyToManyField(Fantasy, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f"{self.name}"