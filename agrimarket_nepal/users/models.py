from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import UserManager


class User(AbstractUser):
    class RoleTypes(models.TextChoices):
        Farmer = "Farmer", _("Farmer")
        Consumer = "Consumer", _("Consumer")
        Admin = "Admin", _("Admin")

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

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.username
