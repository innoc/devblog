from django.shortcuts import render
from .models import ImagePost

# Create your views here.

def post_list(request):
	image_post = ImagePost.objects.all()
	return render(request,'devblog/post_list.html', {'posts':image_post})


def detail(request, post_id):
	return render(request, 'devblog/post_detail.html', {})