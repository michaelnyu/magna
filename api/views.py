from django.shortcuts import render
from rest_framework import viewsets

from api.models import Character
from api.serializers import CharacterSerializer

class CharacterViewSet(viewsets.ModelViewSet):
	"""
	API endpoint that allows users to be viewed or edited.
	"""
	queryset = Character.objects.all()
	serializer_class = CharacterSerializer