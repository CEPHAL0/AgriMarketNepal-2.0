from django.shortcuts import render
from .serializers import ProvinceSerializer
from .models import Province
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.


class ProvinceList(APIView):
    """
    List all Provinces, or create a new Province.
    """

    def get(self, request, format=None):
        provinces = Province.objects.all()
        serializer = ProvinceSerializer(provinces, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ProvinceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
