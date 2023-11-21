from django import forms
# Import the CustomUser model or replace with your model
from accounts.models import CustomUser
from django.forms.widgets import RadioSelect
from django.contrib.auth.forms import UserCreationForm


class FirstOnboardingForm(forms.ModelForm):
    class Meta:
        model = CustomUser  # Replace with your actual model
        fields = ['age', 'gender', 'phone_number',
                  'location', 'bio', 'interests']


class SecondOnboardingForm(forms.ModelForm):
    cleanliness_level = forms.ChoiceField(
        choices=CustomUser.CLEANLINESS_CHOICES,  # Assuming you have CLEANLINESS_CHOICES in your model
        widget=RadioSelect,
        label="What is your Cleanliness Level?"  # Custom label for the entire field
    )

    smoking_preference = forms.ChoiceField(
        choices=CustomUser.SMOKING_CHOICES,  # Assuming you have SMOKING_CHOICES in your model
        widget=RadioSelect,
        label="What is your Smoking Preference?"
    )

    pet_friendly = forms.ChoiceField(
        choices=CustomUser.PET_FRIENDLY_CHOICES,  # Assuming you have PET_FRIENDLY_CHOICES in your model
        widget=RadioSelect,
        label="Do you like pets?"
    )

    class Meta:
        model = CustomUser  # Replace with your actual model
        fields = [
            'cleanliness_level',
            'smoking_preference',
            'pet_friendly',
        ]


class ThirdOnboardingForm(forms.ModelForm):

    introverted_or_extroverted = forms.ChoiceField(
        label="Are you introverted, extroverted, or an ambivert?",  # Custom label
        choices=CustomUser.INTROVERTED_CHOICES,
        widget=RadioSelect
    )
    conflict_resolution_style = forms.ChoiceField(
        label="How do you typically handle conflicts?",  # Custom label
        choices=CustomUser.CONFLICT_RESOLUTION_CHOICES,
        widget=RadioSelect
    )
    communication_preferences = forms.ChoiceField(
        label="What are your communication preferences in resolving issues?",  # Custom label
        choices=CustomUser.COMMUNICATION_CHOICES,
        widget=RadioSelect
    )

    class Meta:
        model = CustomUser  # Replace with your actual model
        fields = [
            'introverted_or_extroverted',
            'conflict_resolution_style',
            'communication_preferences',
        ]
        
class FourthOnboardingForm(forms.ModelForm):

    room_type_preference = forms.ChoiceField(
        label="What type of room do you prefer?",  # Custom label
        choices=CustomUser.ROOM_TYPE_CHOICES,
        widget=RadioSelect
    )
    room_furniture_preference = forms.ChoiceField(
        label="How do you like your rooms like?",  # Custom label
        choices=CustomUser.ROOM_FURNITURE_CHOICES,
        widget=RadioSelect
    )

    class Meta:
        model = CustomUser  # Replace with your actual model
        fields = [
            'room_type_preference',
            'room_furniture_preference',
        ]


class SuperuserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email',)