from rest_framework import serializers
from .models import GenshinChar

class GenshinCharSerializer(serializers.ModelSerializer):
    class Meta:
        model = GenshinChar
        fields = ['id', 'name', 'stars', 'element', 'weapon']