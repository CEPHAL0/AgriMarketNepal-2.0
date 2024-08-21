from django.urls import path
from .views import AuthList, Register
from rest_framework.routers import DefaultRouter

urlpatterns = [path("login", AuthList.as_view()), path("register", Register.as_view())]
