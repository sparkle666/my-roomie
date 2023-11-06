import profile
from django.contrib.auth.models import AbstractUser
from django.db import models


class Interest(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class CustomUser(AbstractUser):

    # Gender Choices
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Non-binary', 'Non-binary'),
        ('Other', 'Other')
    ]

    # Lifestyle Choices
    CLEANLINESS_CHOICES = [
        ('Very neat', 'Very neat'),
        ('Moderately neat', 'Moderately neat'),
        ('Messy', 'Messy')
    ]

    SMOKING_CHOICES = [
        ('Non-smoker', 'Non-smoker'),
        ('Smoker', 'Smoker')
    ]

    PET_FRIENDLY_CHOICES = [
        ('Pet-friendly', 'Pet-friendly'),
        ('Not pet-friendly', 'Not pet-friendly')
    ]

    # Introverted/Extroverted Choices
    INTROVERTED_CHOICES = [
        ('Introverted', 'Introverted'),
        ('Extroverted', 'Extroverted'),
        ('Ambivert', 'Ambivert')
    ]

    # Conflict Resolution Style Choices
    CONFLICT_RESOLUTION_CHOICES = [
        ('Calm and diplomatic', 'Calm and diplomatic'),
        ('Direct and assertive', 'Direct and assertive'),
        ('Avoidant', 'Avoidant')
    ]

    # Communication Preferences Choices
    COMMUNICATION_CHOICES = [
        ('Open and direct', 'Open and direct'),
        ('Polite and indirect', 'Polite and indirect'),
        ('Non-confrontational', 'Non-confrontational')
    ]

    # Room Furniture Preference Choices
    ROOM_FURNITURE_CHOICES = [
        ('Furnished', 'Furnished'),
        ('Unfurnished', 'Unfurnished')
    ]
    ROOM_TYPE_CHOICES = [
        ('Self Contain', 'Self Contain'),
        ('Flat House', 'Flat House')]

    # Personal Information
    age = models.PositiveIntegerField(null=True)
    gender = models.CharField(max_length=20, choices=GENDER_CHOICES, null=True)
    phone_number = models.CharField(max_length=200, null=True)
    location = models.CharField(max_length=200, null=True)
    bio = models.CharField(max_length=200, null=True)
    interests = models.ManyToManyField(Interest, blank=True, null=True)
    profile_photo = models.ImageField(upload_to="images", null=True)

    # Lifestyle Preferences
    cleanliness_level = models.CharField(
        max_length=20, choices=CLEANLINESS_CHOICES, null=True)
    dietary_preferences = models.CharField(max_length=200, null=True)
    smoking_preference = models.CharField(
        max_length=20, choices=SMOKING_CHOICES, null=True)
    pet_friendly = models.CharField(
        max_length=20, choices=PET_FRIENDLY_CHOICES, null=True)

    # Personality and Compatibility
    introverted_or_extroverted = models.CharField(
        max_length=20, choices=INTROVERTED_CHOICES, null=True)
    conflict_resolution_style = models.CharField(
        max_length=20, choices=CONFLICT_RESOLUTION_CHOICES, null=True)
    communication_preferences = models.CharField(
        max_length=20, choices=COMMUNICATION_CHOICES, null=True)

    # Room Preferences
    room_type_preference = models.CharField(
        max_length=20, choices=ROOM_TYPE_CHOICES, null=True)
    room_furniture_preference = models.CharField(
        max_length=20, choices=ROOM_FURNITURE_CHOICES, null=True)

    def __str__(self):
        return self.email


class RoommateMatch(models.Model):
    roommate1 = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name='match1', null=True)
    roommate2 = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name='match2',  null=True)
    match_score = models.FloatField()
    is_matched = models.BooleanField(default=False)
