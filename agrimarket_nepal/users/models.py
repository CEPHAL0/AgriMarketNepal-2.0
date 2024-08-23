from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import UserManager
from django.contrib.auth.models import BaseUserManager


class RoleTypes(models.TextChoices):
    Farmer = "Farmer", _("Farmer")
    Consumer = "Consumer", _("Consumer")
    Admin = "Admin", _("Admin")


class MyUserManager(BaseUserManager):
    def create_user(
        self, email, username, password=None, role=RoleTypes.Consumer, **extra_fields
    ):
        if not email:
            raise ValueError("Users must have email address")

        user = self.model(
            email=self.normalize_email(email),
            username=username,
            role=role,
            **extra_fields,
        )

        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, username, password=None, **extra_fields):
        extra_fields.setdefault("role", RoleTypes.Admin)
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        user = self.create_user(email, username, password, **extra_fields)
        user.save()
        return user


class User(AbstractUser):
    class Meta:
        db_table = "users"

    id = models.BigAutoField(primary_key=True)
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=20, choices=RoleTypes)
    password = models.CharField(max_length=100)
    image = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = MyUserManager()

    USERNAME_FIELD = "email"
    EMAIL_FIELD = "email"
    REQUIRED_FIELDS = ["username", "password"]

    def __str__(self):
        return self.username
