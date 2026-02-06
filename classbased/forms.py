from django import forms
from django.contrib.auth.forms import PasswordChangeForm
from classbased.models import Profile


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['phone', 'city']
