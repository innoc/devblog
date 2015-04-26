from django.shortcuts import render
from devblog.models import ImagePost
from devblog.models import VideoPost
from devblog.models import UserAdditionalInfo
from django.contrib.auth.models import User

from django.http import Http404
import logging


logger = logging.getLogger("django.request")

def post_list(request):
	"""
	DESCRIPTION
	............

	This method generates a list of post. The list is displayed in ascending order
	"""
	image_post_list = list(ImagePost.objects.all())
	video_post_list = list(VideoPost.objects.all())
	all_post = image_post_list + video_post_list
	return render(request,'devblog/post_list.html', {'posts':all_post})


def detail(request, post_id, post_type):
	"""
	DESCRIPTION
	............

	This method displays more information about a particular post.

	PARAMETER
	............

	Post_id : The id integer of the post to be displayed
	post_type : This parameter shows if the post is a video post or an image post
	"""

	user_additional_info = UserAdditionalInfo.objects.get(user_id = 1)
	user = User.objects.get(id=1)
	try:
		if post_type == "i": # i represents images
			post = ImagePost.objects.get(id = post_id)
		else:
			post = VideoPost.objects.get(id = post_id)
	except (ImagePost.DoesNotExist, VideoPost.DoesNotExist):
		logger.error('Something went wrong!')
		raise Http404("Post does not exist")
	return render(request, 'devblog/post_detail.html', {'post':post, 'extra_info':user_additional_info,'author':user})
