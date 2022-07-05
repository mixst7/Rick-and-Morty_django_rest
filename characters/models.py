from django.db import models
from django.contrib.auth.models import User


class Location(models.Model):
    title = models.CharField(max_length=255)
    universe = models.CharField(max_length=255)
    desc = models.TextField()
    image = models.ImageField(upload_to='images', blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Character(models.Model):

    MALE = 'ML'
    FEMALE = 'FL'
    GENDERLESS = 'GS'

    CHOICES_LIVE = [
        ('AL', 'Alive'),
        ('DD', 'Dead'),
        ('UN', 'Unknown')
    ]

    CHOICE_GENDER = [
        (MALE, 'Male'),
        (FEMALE, 'Female'),
        (GENDERLESS, 'Genderless'),
        ("UN", 'Unknown')
    ]


    name = models.CharField(max_length=255)
    status = models.CharField(choices=CHOICES_LIVE, max_length=3, default='UN')
    desc = models.TextField()
    gender = models.CharField(choices=CHOICE_GENDER, max_length=11, default="UN")
    race = models.CharField(max_length=255, blank=True, null=True)
    birth_location = models.ForeignKey(Location, related_name='birth_location', on_delete=models.CASCADE)
    current_location = models.ForeignKey(Location, related_name='current_location', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Episode(models.Model):
    title = models.CharField(max_length=255)
    number_episode = models.IntegerField(verbose_name='номер серии')
    desc = models.TextField(blank=True, null=True)
    characters = models.ManyToManyField(Character, null=True, blank=True)
