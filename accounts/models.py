from django.contrib.auth.models import AbstractUser
from django.db import models


class Interest(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    bio = models.CharField(max_length=200)
    interests = models.ManyToManyField(Interest, blank=True)

    def __str__(self):
        return self.email


class RoommateMatch(models.Model):
    roommate1 = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name='match1', null=True)
    roommate2 = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name='match2',  null=True)
    match_score = models.FloatField()
    is_matched = models.BooleanField(default=False)
