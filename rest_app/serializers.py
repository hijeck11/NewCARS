from rest_framework import serializers
from .models import AutohausREST

class MyModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = AutohausREST
        fields = '__all__'
