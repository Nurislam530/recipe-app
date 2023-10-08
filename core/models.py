from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

class Recipe(models.Model):
    name = models.CharField(max_length=120)
    image = models.ImageField()
    ingredients = models.TextField()
    description = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Comment(models.Model):
    stars = models.DecimalField(decimal_places=1, max_digits=2)
    description = models.TextField(blank = True, null=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)

    def __str__(self):
        return self.description