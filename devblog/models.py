from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class basePost(models.Model):
	"""
		DESCRIPTION
		.............
		This is an abstract class that acts as a base class for the classes below. It extracts common 
		information from ImagePost and VideoPost and assigns these imformation when 
		a new instance of ImagePost or VideoPost is created.
	"""
	
	CATEGORY_CHOICES = (
		('bk', 'Backend development'),
		('fr', 'Frontend development'),
		('gr','Graphic design'),
	)

	author = models.ForeignKey('auth.User', default=0)
	description = models.TextField(default="null")
	category = models.CharField(max_length=5, choices=CATEGORY_CHOICES,default="bk")
	created_date = models.DateTimeField(default=timezone.now)

	def publish(self):
	  self.created_date = timezone.now()
	  self.save()

	def __str__(self):
	  return self.title

	class Meta:
		abstract = True

class ImagePost(basePost):
	"""
		This class Inherits from abstract parent class (basePost)
	"""  
	image = models.ImageField(upload_to='.')


class VideoPost(basePost):
	"""
		This class inherits from abstract parent class (basePost)
	"""
	v_id = models.CharField(max_length=100)