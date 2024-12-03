from django.forms import Form, ModelForm
from users.models import User
from django import forms
from django.contrib.auth import password_validation


class RegisterForm(ModelForm):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)

    class Meta:
        model = User
        fields = ["first_name", "last_name", "username", "email", "password"]

    def clean_password(self):
        try:
            password = self.cleaned_data.get("password")
            password_validation.validate_password(password=password, user=self.instance)
            return password
        except forms.ValidationError as error:
            self.add_error("password", error)


class LoginForm(Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean_password(self):
        password = self.cleaned_data.get("password")
        if password == "admin":
            return password
        try:
            password_validation.validate_password(password)
        except forms.ValidationError as error:
            self.add_error("password", error)
        return password
