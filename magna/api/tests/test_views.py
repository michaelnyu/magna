import json
from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse
from ..models import UserEntry
from ..serializers import UserEntrySerializer


# initialize the APIClient app
client = Client()

class GetAllPuppiesTest(TestCase):
	""" Test module for GET all entries endpoint """

	def setUp(self):
		UserEntry.objects.create(
			name='u1', donation=22, text="beautiful soup1")
		UserEntry.objects.create(
			name='u2', donation=0, text="beautiful soup2")
		UserEntry.objects.create(
			name='u3', donation=50, text="beautiful soup3")
		UserEntry.objects.create(
			name='u4', donation=99, text="beautiful soup4")



	def test_get_all_entries(self):
		# get API response
		response = client.get(reverse('get_post_user_entry'))
		# get data from db
		entries = UserEntry.objects.all()
		serializer = UserEntrySerializer(entries, many=True)
		self.assertEqual(response.data, serializer.data)
		self.assertEqual(response.status_code, status.HTTP_200_OK)

	def test_get_invalid_single_entry(self):
		response = client.get(
			reverse('get_delete_put_user_entry', kwargs={'pk': 30}))
		self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)