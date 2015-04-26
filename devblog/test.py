from django.test import TestCase
from devblog.models import ImagePost
from devblog.models import VideoPost
from devblog.models import UserAdditionalInfo
from django.contrib.auth.models import User


class TestApp(TestCase):
	"""
		DESCRIPTION
		............
		These test cases are used to test the creation of image and video post objects.
		It is also used to test the creation of user additional info
	"""
	
	def setUp(self):
		user = User.objects.create(username="Innocent")
		ImagePost.objects.create(author=user, description="testing testing", category="bk", title="i")
		VideoPost.objects.create(author=user, description="testing testing", category="bk", title="v")
		UserAdditionalInfo.objects.create(user=user, description="yay")
	
	def test_post_existence(self):
		"""The post created above acctually exist"""
		image = ImagePost.objects.get(title="i")
		video = VideoPost.objects.get(title="v")
		self.assertIsNotNone(image)
		self.assertIsNotNone(video)

	def test_user_addition_info(self):
		"""A user can succesfully create addiytional info"""
		info = UserAdditionalInfo.objects.get(description="yay")
		self.assertIsNotNone(info)