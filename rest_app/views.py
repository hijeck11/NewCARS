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

    def get_queryset(self):
        queryset = AutohausREST.objects.all()
        q = self.request.query_params.get('q', None)
        if q:
            queryset = queryset.filter(brand_auto__icontains=q)
        return queryset