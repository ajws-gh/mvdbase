from django import forms
from .models import Ratings


class RatingForm(forms.ModelForm):
    class Meta:
        model = Ratings
        exclude = ['user', 'actor']
