from django import forms
from .models import Person, Profile
from django.contrib.auth.models import User


class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['name', 'color']

# class UserForm(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = ['username', 'email']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['location']