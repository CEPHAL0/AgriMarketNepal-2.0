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
        password = self.cleaned_data.get("password")
        try:
            password_validation.validate_password(password=password, user=self.instance)
        except forms.ValidationError as error:
            self.add_error("password", error)
        return password
