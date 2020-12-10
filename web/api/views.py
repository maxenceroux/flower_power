from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics, status

from rest_framework.views import APIView
from .models import Flower
from .serializers import FlowerSerializer, CreateFlowerSerializer
from rest_framework.response import Response

# Create your views here.

class FlowerView(generics.ListAPIView):
    queryset = Flower.objects.all()
    serializer_class = FlowerSerializer

class CreateFlowerView(APIView):
    serializer_class = CreateFlowerSerializer
    def post(self, request, format=None):
        if not self.request.session.exists(self.request.session.session_key):
            self.request.session.create()
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            name = serializer.data.get('name')
            type = serializer.data.get('type')
            queryset = Flower.objects.filter(name=name)
            if queryset.exists():
                return Response({'Bad Request': 'Flower with same name already exists'}, status=status.HTTP_400_BAD_REQUEST)
            else: 
                flower = Flower(name=name, type=type)
                flower.save()
                return Response(FlowerSerializer(flower).data, status=status.HTTP_201_CREATED)
        return Response({'Bad Request': 'Invalid Data'}, status=status.HTTP_400_BAD_REQUEST)

def main(request):
    return HttpResponse("hello")