from django.db import models

class Character(models.Model):
	created = models.DateTimeField(auto_now_add=True)
