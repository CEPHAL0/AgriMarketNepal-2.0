from django.urls import path
from .views import (
    AuthList,
    LoginView,
    Register,
    RegisterResponseView,
    UserList,
    RegisterView,
)
from rest_framework.routers import DefaultRouter

app_name = "users"
api_urlpatterns = [
    path("login", AuthList.as_view()),
    path("register", Register.as_view()),
    path("", UserList.as_view({"get": "list"})),
]

urlpatterns = [
    path("register", RegisterView.as_view(), name="register"),
    path("create", RegisterView.as_view(), name="create"),
    path("login", LoginView.as_view(), name="login"),
    path("authenticate", LoginView.as_view(), name="authenticate"),
]
