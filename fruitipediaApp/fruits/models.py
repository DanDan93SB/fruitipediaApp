from django.core.validators import MinLengthValidator
from django.db import models

from fruitipediaApp.fruits.validators import only_letters_validator


class Category(models.Model):
    name = models.CharField(
        max_length=255,
        unique=True,
    )

    def __str__(self):
        return self.name


class Fruit(models.Model):
    name = models.CharField(
        max_length=30,
        validators=[
            MinLengthValidator(2),
            only_letters_validator,
        ],
    )

    image_url = models.URLField()

    description = models.TextField()

    nutrition = models.TextField(
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.name