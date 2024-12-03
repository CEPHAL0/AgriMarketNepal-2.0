from django.shortcuts import redirect, render
from django.urls import reverse
from rest_framework.response import Response
from .serializers import UserSerializer, AuthSerializer, RegisterSerializer
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, response
from .models import RoleTypes, User
from users.forms import RegisterForm, LoginForm
from django.views import View
from django.contrib import messages


class RegisterView(View):
    def get(self, request):
        form = RegisterForm()
        return render(request, "auth/register.html", {"form": form})

    def post(self, request):
        data = request.POST
        form = RegisterForm(data)

        if form.is_valid():
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            username = form.cleaned_data["username"]
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]

            user = User.objects.create_user(
                username=username,
                email=email,
                password=password,
                first_name=first_name,
                last_name=last_name,
            )

            messages.success(request, "User successfully registered")

            return redirect("users:register")
        else:
            ctx = {"form": form}
            return render(request, "users/name.html", ctx)


class LoginView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, "auth/login.html", {"form": form})

    def post(self, request):
        data = request.POST
        form = LoginForm(data)

        try:
            if form.is_valid():
                email = form.cleaned_data["email"]
                password = form.cleaned_data["password"]

                user = authenticate(username=email, password=password)

                if user is None:
                    messages.error(request, "Invalid Credentials")
                    raise Exception("Invalid Credentials")
                else:
                    login(request, user)
                    if user.role == "Admin":
                        return redirect("consumables:admin:home")
            else:
                raise Exception("Form Invalid")

        except Exception as error:
            ctx = {"form": form}
            return render(request, "auth/login.html", ctx)


class AdminHomeView(View):
    def get(self, request):
        return HttpResponse({"message": "Hello World From Admin"})


class FarmerView(View):
    def get(self, request):
        return {"message": "Hello World From Farmer"}


class LogoutView(View):
    def post(self, request):
        logout(request)
        return redirect(reverse("users:login"))


class RegisterResponseView(View):
    def get(self, request):
        print("Hello world")
        return response({"message": "Hello World"})
