from django.contrib import admin
from .models import ImagePost
from .models import VideoPost
from .models import UserAdditionalInfo

from django.contrib.auth.models import User

admin.site.register(ImagePost)
admin.site.register(VideoPost)
admin.site.register(UserAdditionalInfo)