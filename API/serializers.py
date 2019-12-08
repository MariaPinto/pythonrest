from rest_framework import serializers

from API.models import Person


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model= Person
        fields= ["id", "username", "email", "password", "imagen"]


