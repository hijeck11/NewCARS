from rest_framework import serializers
from .models import AutohausREST

class MyModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = AutohausREST
        fields = '__all__'
    auto_img = serializers.ImageField(use_url=True)