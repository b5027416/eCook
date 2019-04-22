from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Review(models.Model):
	date_submitted=models.DateTimeField(default=timezone.now)
	author=models.ForeignKey(User, on_delete=models.CASCADE)
	rating=models.CharField (max_length=100)
	reviewText=models.TextField()


	def __str__ (self):
		return self.reviewText


# Create your models here.
