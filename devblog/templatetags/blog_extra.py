from django import template
from django.contrib.auth.models import User
from devblog.models import ImagePost
from devblog.models import UserAdditionalInfo
from devblog.models import VideoPost

register = template.Library()

@register.inclusion_tag('devblog/header.html')

def generate_header_content():
	"""
	DESCRIPTION
	............

	This method is a custom template method that is reuseable in any template that loads it. It's function is to generate the contents needed for the header
	"""

	user_additional_info = UserAdditionalInfo.objects.get(user_id = 1)
	user = User.objects.get(id=1)
	image_post_list = list(ImagePost.objects.all())
	video_post_list = list(VideoPost.objects.all())
	all_post = image_post_list + video_post_list
	return {'owner_primary_info': user,'owner_extra_info': user_additional_info, 'image_post_count': image_post_list, 'video_post_count': video_post_list} 