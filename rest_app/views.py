from django.shortcuts import render
from rest_framework import generics
from .models import AutohausREST
from .serializers import MyModelSerializer


class MyModelListCreateView(generics.ListCreateAPIView):
    queryset = AutohausREST.objects.all()
    serializer_class = MyModelSerializer
