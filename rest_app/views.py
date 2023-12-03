from django.shortcuts import render
from rest_framework import generics
from .models import AutohausREST
from .serializers import MyModelSerializer


class MyModelListCreateView(generics.ListCreateAPIView):
    queryset = AutohausREST.objects.all()
    serializer_class = MyModelSerializer

    def list(self, request, *args, **kwargs):
        cars_list = self.get_queryset()
        return render(request, 'cars_list.html', {'cars_list': cars_list})