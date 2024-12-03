from django.urls import include, path
from .views import (
    AdminHomeView,
    LoginView,
    LogoutView,
    RegisterResponseView,
    RegisterView,
)
from rest_framework.routers import DefaultRouter

app_name = "users"

urlpatterns = [
    path("register", RegisterView.as_view(), name="register"),
    path("create", RegisterView.as_view(), name="create"),
    path("login", LoginView.as_view(), name="login"),
    path("logout", LogoutView.as_view(), name="logout"),
    path("authenticate", LoginView.as_view(), name="authenticate"),
]
