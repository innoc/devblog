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

	POST_TYPE = (
		('i', 'image'),
		('v', 'video'),
	)

	author = models.ForeignKey('auth.User', default=0)	
	description = models.TextField(default="enter a value")
	category = models.CharField(max_length=5, choices=CATEGORY_CHOICES,default="bk")
	created_date = models.DateTimeField(default=timezone.now)
	title = models.CharField(max_length=100)
	post_type = models.CharField(max_length=5, choices=POST_TYPE,default="")


	class Meta:
		abstract = True


class ImagePost(basePost):
	"""
		DESCRIPTION
		............
		This class Inherits from abstract parent class (basePost)
	"""  
	image = models.ImageField(upload_to='imagefile/')


	def publish(self):
	  self.created_date = timezone.now()
	  self.save()

	def __str__(self):
	  return str(self.author)


class VideoPost(basePost):
	"""
		DESCRIPTION
		............
		This class inherits from abstract parent class (basePost)
	"""
	v_id = models.CharField(max_length=100)

	def publish(self):
	  self.created_date = timezone.now()
	  self.save()

	def __str__(self):
	  return str(self.author)


class UserAdditionalInfo(models.Model):
	"""
		DESCRIPTION
		............
		This class holds more information about the blog user
	"""
	CATEGORY_CHOICES = (
		('m', 'Male'),
		('f', 'Female'),
	)
	image = models.ImageField(upload_to='imagefile/')
	user = models.ForeignKey('auth.User', default=0)
	description = models.TextField(default="null")
	gender = models.CharField(max_length=2, choices=CATEGORY_CHOICES, default="m")

	def __str__(self):
		return str(self.user)