from django.db.models import F
from django.shortcuts import get_object_or_404

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import requests

from .models import UserEntry
from .serializers import UserEntrySerializer
from django.db.models import Sum

from .sentiment import listEntities, showSentiment



@api_view(['GET', 'DELETE', 'PUT'])
def get_delete_put_user_entry(request, pk):
	try:
		user_entry = UserEntry.objects.get(pk=pk)
	except UserEntry.DoesNotExist:
		return Response(status=status.HTTP_404_NOT_FOUND)

	# get details of specified User Entry
	if request.method == 'GET':
		serializer = UserEntrySerializer(user_entry)
		return Response(serializer.data)
	# delete specified User Entry
	elif request.method == 'DELETE':
		user_entry.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)
	# update details of a specified User Entry
	elif request.method == 'PUT':
		serializer = UserEntrySerializer(user_entry, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def get_post_user_entry(request):
	# get all entries
	if request.method == 'GET': 
		entries = UserEntry.objects.all()
		serializer = UserEntrySerializer(entries, many=True)
		return Response(serializer.data)
	# create a new user entry in our table
	elif request.method == 'POST':
		text = request.data.get('text')
		data = {
			'name': request.data.get('name'),
			'donation': int(request.data.get('donation')),
			'text': text,
			'character_name': request.data.get('character').get('name'),
			'character': request.data.get('character'),
			'entities' : listEntities(text),
			'sentiment_score' : showSentiment(text)[0],
			'sentiment_magnitude' : showSentiment(text)[1],
		}

		serializer = UserEntrySerializer(data=data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_top_donors(request, number):
	""" Get the top 'n' donors """
	if request.method == 'GET':
		entries = UserEntry.objects.all()
		if len(entries) > int(number):
			donors = entries.order_by('-donation')[:int(number)]
		else:
			donors = entries.order_by('-donation')[:len(entries)]
		top_users = [user for user in donors if user.donation != 0]
		serializer = UserEntrySerializer(top_users, many=True)
		data = {
			'entries' : serializer.data,
		}
		return Response(data, status=status.HTTP_200_OK)
	return Response(status=status.HTTP_400_BAD_REQUEST)

#New Code for revised User Entries
@api_view(['GET'])
def get_users_by_name(request, name):
	""" Get all users in a specified region """
	if request.method == 'GET':
		entries = UserEntry.objects.filter(name=name)
		if len(entries) == 0:
			return Response(status=status.HTTP_404_NOT_FOUND)
		serializer = UserEntrySerializer(entries, many=True)
		return Response(serializer.data)
		
	return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_latest_donors(request, number):
	""" Get most recent 'n' donors """
	if request.method == 'GET':
		entries = UserEntry.objects.filter(donation__gt=0)
		if len(entries) > int(number):
			donors = entries.order_by('-pk')[:int(number)]
		else:
			donors = entries.order_by('-pk')[:len(entries)]
		latest_users = [user for user in donors]
		serializer = UserEntrySerializer(latest_users, many=True)
		data = {
			'entries' : serializer.data,
		}
		return Response(data, status=status.HTTP_200_OK)
	return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_total_donations(request):
	""" Get sum of all donations """
	if request.method == 'GET':
		s = UserEntry.objects.aggregate(total=Sum('donation'))['total'] or 0
		payload = {
			'total': s,
		}
		return Response(payload, status=status.HTTP_200_OK)
	return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_recent_entries(request, number):
	""" get most recent 'n' elements that have been added
	"""
	
	if request.method == 'GET':
		_recent = UserEntry.objects.all().order_by('-created_at')

		if len(_recent) > int(number):
			_recent = _recent[:int(number)]
		else:
			_recent = _recent[:len(_recent)]
		_r_entries = [ r for r in _recent ]
		serializer = UserEntrySerializer(_r_entries, many=True)
		data = {
			'entries' : serializer.data,
		}
		return Response(data, status=status.HTTP_200_OK)

	return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def put_vote(request, pk):
	""" Increment the votes count of the entry specified
	"""

	_user_entry = get_object_or_404(UserEntry, pk=pk)

	if request.method == 'PUT':
		_user_entry.votes = F('votes') + 1
		_user_entry.save()
		_user_entry.refresh_from_db()
		return Response(status=status.HTTP_202_ACCEPTED)
