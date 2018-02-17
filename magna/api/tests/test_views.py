import json
from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse
from ..models import UserEntry
from ..serializers import UserEntrySerializer


# initialize the APIClient app
client = Client()

class GetAllUserEntriesTest(TestCase):
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

class CreateNewUserEntryTest(TestCase):
	""" Test module for inserting a new User Entry """

	def setUp(self):
		self.valid_payload = {
			'name': 'Michael',
			'donation': 10,
			'text': 'big big big huge penis',
			'head': 'big',
			'arms': 'small',
			'torso': 'slim',
			'legs': 'tree',
			'shoes': 'chucks',			
		}
		self.invalid_payload = {
			'name': '',
			'donation': 0,
			'text': "small small penis"
		}

	def test_create_valid_user_entry(self):
		response = client.post(
			reverse('get_post_user_entry'),
			data=json.dumps(self.valid_payload),
			content_type='application/json'
		)
		self.assertEqual(response.status_code, status.HTTP_201_CREATED)

	def test_create_invalid_user_entry(self):
		response = client.post(
			reverse('get_post_user_entry'),
			data=json.dumps(self.invalid_payload),
			content_type='application/json'
		)
		self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

class UpdateSingleUserEntryTest(TestCase):
	""" Test module for updating an existing user entry record """

	def setUp(self):
		self.u1 = UserEntry.objects.create(
			name='u1', donation=22, text="beautiful soup1")
		self.u2 = UserEntry.objects.create(
			name='u2', text="beautiful soup2")
		self.valid_payload = {
			'name': 'Michael',
			'donation': 10,
			'text': 'big big big huge penis',
		}
		self.invalid_payload = {
			'name': '',
			'donation': 0,
			'text': "small small penis"
		}

	def test_valid_update_user_entry(self):
		response = client.put(
			reverse('get_delete_put_user_entry', kwargs={'pk': self.u1.pk}),
			data=json.dumps(self.valid_payload),
			content_type='application/json'
		)
		self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

	def test_invalid_update_user_entry(self):
		response = client.put(
			reverse('get_delete_put_user_entry', kwargs={'pk': self.u1.pk}),
			data=json.dumps(self.invalid_payload),
			content_type='application/json')
		self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class DeleteSingleUserEntryTest(TestCase):
	""" Test module for deleting an existing user entry record """

	def setUp(self):
		self.u1 = UserEntry.objects.create(
			name='u1', donation=22, text="beautiful soup1")

	def test_valid_delete_user_entry(self):
		response = client.delete(
			reverse('get_delete_put_user_entry', kwargs={'pk': self.u1.pk}))
		self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

	def test_invalid_delete_user_entry(self):
		response = client.delete(
			reverse('get_delete_put_user_entry', kwargs={'pk': 66}))
		self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

class GetRecentUserEntryTest(TestCase):
	""" Test module for most getting 'n' most recent entries
	"""

	def setUp(self):
		self.u1 = UserEntry.objects.create(
			name='u1', donation=22, text="beautiful soup1")
		self.u2 = UserEntry.objects.create(
			name='u2', text="beautiful soup2")
		self.u3 = UserEntry.objects.create(
			name='u3', donation=50, text="beautiful soup3")
		self.u4 = UserEntry.objects.create(
			name='u4', donation=99, text="beautiful soup4")

	def test_valid_recent_user(self):
		response = client.get(
			reverse('get_recent_entries', kwargs={'number': 2}))
		self.assertEqual(response.status_code, status.HTTP_200_OK)

	def test_valid_recent_user(self):
		response = client.get(
			reverse('get_recent_entries', kwargs={'number': 6}))
		self.assertEqual(response.status_code, status.HTTP_200_OK)

