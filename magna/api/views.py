
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import UserEntry
from .serializers import UserEntrySerializer
from django.db.models import Sum

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
		data = {
			'name': request.data.get('name'),
			'donation': int(request.data.get('donation')),
			'text': request.data.get('text'),
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
		top_users = [user.id for user in donors if user.donation != 0]
		return Response(top_users, status=status.HTTP_200_OK)
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
		latest_users = [user.id for user in donors]
		return Response(latest_users, status=status.HTTP_200_OK)
	return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_total_donations(request):
	""" Get sum of all donations """
	if request.method == 'GET':
		entries = UserEntry.objects.aggregate(total=Sum('donation'))['total'] or 0
		return Response(entries, status=status.HTTP_200_OK)
	return Response(status=status.HTTP_400_BAD_REQUEST)

