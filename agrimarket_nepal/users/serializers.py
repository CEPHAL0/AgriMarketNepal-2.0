from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "email", "role", "password", "image"]

    def __str__(self):
        return self.username


class AuthSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()


class RegisterSerializer(serializers.Serializer):
    email = serializers.EmailField()
    username = serializers.CharField()
    password = serializers.CharField()
    password_confirm = serializers.CharField()

    def validate_username(self, value):
        userExists = User.objects.filter(username=value).exists()
        if userExists:
            raise serializers.ValidationError("Username already exists")
        return value

    def validate_email(self, value):
        userExists = User.objects.filter(email=value).exists()
        if userExists:
            raise serializers.ValidationError("Email already registered")
        return value

    def validate(self, data):
        if data["password"] != data["password_confirm"]:
            raise serializers.ValidationError("Password confirmation does not match")
        return data
