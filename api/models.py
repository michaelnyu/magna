from django.db import models

class Character(models.Model):
	created = models.DateTimeField(auto_now_add=True)
	firstname = models.CharField(max_length=30, default='')
	lastname = models.CharField(max_length=30, blank=True, default='')
	donation = models.IntegerField(blank=True, default=0)

	head = models.CharField(max_length=100, blank=True, default='')
	leftarm = models.CharField(max_length=100, blank=True, default='')
	rightarm = models.CharField(max_length=100, blank=True, default='')
	torso = models.CharField(max_length=100, blank=True, default='')
	legs = models.CharField(max_length=100, blank=True, default='')
	shoes = models.CharField(max_length=100, blank=True, default='')
	


	def __str__(self):
		return self.firstname + ' ' + self.lastname;

	class Meta:
		ordering = ('created',)

