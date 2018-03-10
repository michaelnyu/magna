from rest_framework import serializers
from .models import UserEntry


class UserEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = UserEntry
        fields = ('id', 'name', 'donation', 'text', 'character_name', 'character', 'entities', 'votes', 'created_at', 'updated_at')
