from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [ 
	url(
		regex=r'^$',
		view=views.post_list,
		name=""
	),
	url(
		regex=r'^detail/(?P<post_id>\d+)/(?P<post_type>[-\w]+)/$', 
		view=views.detail, 
		name='detail'
	),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)