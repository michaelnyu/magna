from rest_framework import serializers
from .models import UserEntry


class UserEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = UserEntry
        fields = ('name', 'donation', 'text', 'head', 'arms', 'torso', 'legs', 'shoes' ,'created_at', 'updated_at')