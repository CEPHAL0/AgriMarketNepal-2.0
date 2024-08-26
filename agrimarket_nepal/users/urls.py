from django.urls import path
from .views import AuthList, Register, RegisterResponseView, UserList, RegisterView
from rest_framework.routers import DefaultRouter

app_name = "users"
api_urlpatterns = [
    path("login", AuthList.as_view()),
    path("register", Register.as_view()),
    path("", UserList.as_view({"get": "list"})),
]

urlpatterns = [
    path("register", RegisterView.as_view()),
    path("create", RegisterView.as_view(), name="create"),
]
