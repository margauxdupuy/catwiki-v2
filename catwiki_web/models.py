from django.db import models
from django_countries.fields import CountryField


class Cat(models.Model):
    id_name = models.CharField(max_length=4, unique=True)
    name = models.CharField(max_length=50)
    description = models.TextField()
    wikipedia_url = models.URLField(blank=True, null=True)
    temperament = models.CharField(max_length=100)
    origin = CountryField()
    life_span = models.CharField(max_length=20)
    adaptability = models.IntegerField()
    affection_level = models.IntegerField()
    child_friendly = models.IntegerField()
    grooming = models.IntegerField()
    intelligence = models.IntegerField()
    health_issues = models.IntegerField()
    social_needs = models.IntegerField()
    stranger_friendly = models.IntegerField()

    def __str__(self):
        return f"{self.name}"


class CatImage(models.Model):
    url_image = models.URLField(unique=True, blank=False, null=False)
    cat = models.ForeignKey(Cat, on_delete=models.CASCADE)
    main_image = models.BooleanField(default=False)
