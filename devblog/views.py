from django.shortcuts import render
from .models import ImagePost
from .models import VideoPost
from django.http import Http404
import logging


logger = logging.getLogger(__name__)

def post_list(request):
	image_post = ImagePost.objects.all()
	return render(request,'devblog/post_list.html', {'posts':image_post})


def detail(request, post_id, post_type):
	try:    
		if post_type == "i":
			post = ImagePost.objects.get(id = post_id)
		else:
			post = VideoPost.objects.get(id = post_id)
	except ImagePost.DoesNotExist:
		logger.error('Something went wrong!')
		raise Http404("Post does not exist")
	return render(request, 'devblog/post_detail.html', {'post':post})
