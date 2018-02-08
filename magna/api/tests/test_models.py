from django.test import TestCase
from ..models import UserEntry


class UserEntryTest(TestCase):
	""" Test module for UserEntry model """

	def setUp(self):
		UserEntry.objects.create(
			name='Michael', text='North korea can suck a weiner.', donation=69)
		UserEntry.objects.create(
			name='Mr. Roboto', text='sweg')
		
	def test_user_entry_donation(self):
		user_m = UserEntry.objects.get(name='Michael')
		user_r  = UserEntry.objects.get(name='Mr. Roboto')
		self.assertEqual(
			user_m.get_donation(), "Michael donated: 69")
		self.assertEqual(
			user_r.get_donation(), "Mr. Roboto donated: 0")