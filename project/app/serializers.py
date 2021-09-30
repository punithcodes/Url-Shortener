from rest_framework import serializers
from .models import Url

# Here I have created class Serializer which is responsible for serialization and deserialization. Have used meta class and created ModelSerializer.
class UrlSerializer(serializers.ModelSerializer):
    class Meta:
        model = Url
        fields = '__all__'
