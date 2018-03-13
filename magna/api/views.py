import random
import requests, base64, json

from requests.auth import HTTPBasicAuth
from django.db.models import F
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Sum

from api.models import UserEntry
from api.serializers import UserEntrySerializer
from api.sentiment import listEntities, showSentiment, getSentimentUsers, matchEntities
from django.conf import settings

@api_view(['GET', 'DELETE', 'PUT'])
def get_delete_put_user_entry(request, pk):
	try:
		user_entry = UserEntry.objects.get(pk=pk)
	except UserEntry.DoesNotExist:
		return Response(status=status.HTTP_404_NOT_FOUND)

	# get details of specified User Entry
	if request.method == 'GET':
		serializer = UserEntrySerializer(user_entry)
		res = serializer.data
    
		res["sentiment_users"] = getSentimentUsers(user_entry, pk)
		matches = {}
		for entity in res['entities']:
			matches[entity] = matchEntities(entity, pk)
		res["entity_matches"] = matches
    
		return Response(res)
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

@api_view(['GET']) 
def get_random(request, number):

	if request.method == 'GET':
		allEntries = UserEntry.objects.all()

		if (len(allEntries) > int(number)):
			_random = random.sample(allEntries, int(number))
		else:
			_random = allEntries
		payload = {
			'entries': _random,
		}
		return Response(payload, status=status.HTTP_200_OK)
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

@api_view(['GET'])
def get_rand_users(request, count):

	if request.method == 'GET':
		entries = UserEntry.objects.all() 
		visited = set(0)
		users = set(entries[0])
		visitedNames = set(entries[0].character_name)
		for each in len(entries):
			if len(users) == int(count):
				payLoad = {
					'entries': users
					}
				return Response(payLoad, status=status.HTTP_200_OK)
			if visitedNames.contains(each.character_name):
				continue
			else:
				visited.append(each)
				visitedNames.append(entries[each].character_name)
				users.append(entries[each])
		if len(users) < int(count):
			for each in len(entries):
				if len(users) == int(count):
					payLoad = {
						'entries': users
						}
					return Response(payLoad, status=status.HTTP_200_OK)
				
				if visited.contains(each):
					continue
				else:
					visited.append(each)
					visitedNames.append(entries[each].character_name)
					users.append(entries[each])
		else:
			payLoad = {
				'entries': users
				}

			return Response(payLoad, status=status.HTTP_200_OK)
	return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_unique(request, count):

	if request.method == 'GET':
		character_names_used = set()
		allEntries = UserEntry.objects.all()
		serializer = UserEntrySerializer(allEntries, many=True)
		res_entries = []

		for entry in serializer.data[::-1]:
			if entry['character_name'] not in character_names_used:
				res_entries.append(entry)
				character_names_used.add(entry['character_name'])

		payload = {
			'entries': res_entries[0:int(count)]
		}

		return Response(payload, status=status.HTTP_200_OK)
	return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def create_donation(request):

	payload = json.loads(request.body.decode("utf-8"))

	if request.method == 'POST':
		r = requests.post(
				'https://api.pandapay.io/v1/donations',
				data = json.dumps(payload),
				auth = HTTPBasicAuth(settings.PANDA_KEY, ''),
				headers = {
						'Content-Type': 'application/json; charset=utf-8',
				}
		)

		if r.status_code >= 200 and r.status_code < 300:
			return Response(r.json(), status=status.HTTP_201_CREATED)

	return Response(data=json.dumps(r.text), status=r.status_code)

