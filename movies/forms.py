from .models import Rating
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        exclude = ['user', 'movie']


class UserRegisterForm(UserCreationForm):
    def clean_email(self):
        data = self.cleaned_data['email']
        if User.objects.filter(email=data).exists():
            raise forms.ValidationError("This email already used")
        return data

    def clean_username(self):
        data = self.cleaned_data['username']
        if len(data) > 20:
            raise forms.ValidationError("Please choose shorter username")
        return data

    class Meta:
        model = User
        help_texts = {
            'username': 'Required. 20 characters or fewer. Letters, digits and @/./+/-/_ only.',
            'first_name': 'Max - 150 characters',
            'last_name': 'Max - 150 characters'
        }
        fields = ['first_name', 'last_name', 'username', 'email', ]


class SearchForm(forms.Form):
    search_term = forms.CharField(max_length=255, label='Search for Videos:')


class Subscribe(forms.Form):
    Email = forms.EmailField(help_text='Please provide your e-mail address')
    Subject = forms.CharField(help_text='Max - 150 characters', max_length=40)
    Message = forms.CharField(widget=forms.Textarea(attrs={"rows": 5, "cols": 20}), help_text='Max - 500 characters',
                              max_length=500)
