from django import forms
# Import the CustomUser model or replace with your model
from accounts.models import CustomUser


class FirstOnboardingForm(forms.ModelForm):
    class Meta:
        model = CustomUser  # Replace with your actual model
        fields = ['age', 'gender', 'phone_number',
                  'location', 'bio', 'interests']


class SecondOnboardingForm(forms.ModelForm):
    class Meta:
        model = CustomUser  # Replace with your actual model
        fields = [
            'cleanliness_level',
            'dietary_preferences',
            'smoking_preference',
            'pet_friendly',
        ]
