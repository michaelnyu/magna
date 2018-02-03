from rest_framework import serializers
from api.models import Character


class CharacterSerializer(serializers.ModelSerializer):
	class Meta:
		model = Character
		fields = ('firstname', 'lastname', 'donation', 'head')