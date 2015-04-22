from django.contrib import admin
from .models import ImagePost
from .models import VideoPost

admin.site.register(ImagePost)
admin.site.register(VideoPost)
# Register your models here.