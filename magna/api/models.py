from django.db import models
from django.contrib.postgres.fields import JSONField, ArrayField

class UserEntry(models.Model):
	''' User Entry Model
		Defines attributes of User Entry including:
		donation amount (in cents)
		character description
		name
	'''
	id = models.AutoField(primary_key=True, null=False)
	name = models.CharField(max_length=100)
	text = models.CharField(max_length=255)
	donation = models.IntegerField(default=0)
	votes = models.IntegerField(default=0)
	character_name = models.CharField(max_length=50, default="")
	character = JSONField(default={})
	entities = ArrayField(models.CharField(max_length=200), default=[])

	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def get_donation(self):
		return self.name + ' donated: ' + repr(self.donation)

	def __repr__(self):
		return self.name + ' added'
	
