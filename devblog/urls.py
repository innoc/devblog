from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static
from . import views
from devblog import views

urlpatterns = [ 
	url(r'^$', views.post_list),
	url(r'^detail/(?P<post_id>[0-9]+)/$', views.detail, name='detail'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)