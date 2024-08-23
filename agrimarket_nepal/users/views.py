from django.shortcuts import render
from rest_framework import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request
from .serializers import UserSerializer, AuthSerializer, RegisterSerializer
from django.contrib.auth.decorators import login_not_required
from django.contrib.auth import authenticate
from django.http import Http404
from rest_framework import viewsets
from rest_framework.response import Response
from .models import User
from django.http import HttpResponse
from rest_framework.views import APIView
from agrimarket_nepal.response import BaseApiRenderer, APIResponse
from users.forms import RegisterForm
from django.views import View


class RegisterView(View):
    def get(self, request):
        if request.method == "GET":
            form = RegisterForm()
            return render(request, "name.html", {"form": form})


class AuthView:
    pass


class AuthList(APIView):
    """
    Auth Classes
    """

    def post(self, request, format=None):
        serializer = AuthSerializer(data=request.data)
        if not (serializer.is_valid()):
            return Response(serializer.errors, 400)

        validated_data = serializer.validated_data
        email = validated_data["email"]
        password = validated_data["password"]
        user = authenticate(username=email, password=password)

        if user is not None:
            return APIResponse(data={}, status=200, message="User Found")
        else:
            return APIResponse(data=None, status=404, message="User not found")


class Register(APIView):
    """
    Register a new user
    """

    #    renderer_classes = [BaseApiRenderer]

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if not serializer.is_valid():
            print(serializer.errors)
            return APIResponse(
                data=None,
                status=400,
                message=serializer.errors,
            )
        data = serializer.validated_data

        User.objects.create(
            username=data["username"], email=data["email"], password=data["password"]
        )


class UserList(viewsets.ViewSet):
    def list(self, request):
        queryset = User.objects.all()
        serializer = UserSerializer(queryset, many=True)
        print(serializer)
        return APIResponse(
            data=serializer.data, status=200, message="Users Retrieved Successfully"
        )
