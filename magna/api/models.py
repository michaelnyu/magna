from django.db import models

class UserEntry(models.Model):
	'''
	User Entry Model
	Defines attributes of User Entry including:
		donation amount (in cents)
		character description
		name
	'''

	name = models.CharField(max_length=100)
	text = models.CharField(max_length=255)
	donation = models.IntegerField(default=0)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def get_donation(self):
		return self.name + ' donated: ' + repr(self.donation)

	def __repr__(self):
		return self.name + ' added'