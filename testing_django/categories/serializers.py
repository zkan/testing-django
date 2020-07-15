from rest_framework import serializers

from .models import Category


class CategorySerializer(serializers.Serializer):
    name = serializers.CharField(max_length=300)
    photo = serializers.FileField()
