from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics, status

from rest_framework.views import APIView
from .models import Flower
from .serializers import FlowerSerializer
# Create your views here.

class FlowerView(generics.ListAPIView):
    queryset = Flower.objects.all()
    serializer_class = FlowerSerializer

def main(request):
    return HttpResponse("hello")