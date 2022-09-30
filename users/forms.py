from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from users.models import *


class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = UserProfile
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user


class AddUser(forms.ModelForm):
    class Meta:
        model = UserProfile
        widgets = {
            'password': forms.PasswordInput(),
        }
        fields = ['username', 'password', 'email', 'is_professor', 'is_site_admin']


class EditUser(forms.ModelForm):
    class Meta:
        model = UserProfile
        widgets = {
            'password': forms.PasswordInput(),
        }
        fields = ['username', 'password', 'email', 'is_professor', 'is_site_admin']

    def __init__(self, *args, **kwargs):
        super(EditUser, self).__init__(*args, **kwargs)

        for key in self.fields:
            self.fields[key].required = False


class Contact(forms.Form):
    sender = forms.CharField(label='Name', max_length=30)
    subject = forms.CharField(label='Subject', max_length=30)
    email = forms.EmailField(label='Email', max_length=30)
    message = forms.CharField(widget=forms.Textarea)
