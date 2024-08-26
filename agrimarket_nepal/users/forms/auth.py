from django.forms import Form, ModelForm
from users.models import User
from django import forms


class RegisterForm(ModelForm):
    class Meta:
        model = User
        fields = ["first_name", "last_name", "username", "email", "password"]
