from django.core.management.base import BaseCommand, CommandError
from devblog.models import ImagePost
from devblog.models import VideoPost

class Command(BaseCommand):
	"""
		DESCRIPTION
		...........

		This method prints out a the number of image posts and video post
	"""
	args = ''
	help = 'Displays count into about your posts'

	def handle(self, *args, **options):
		imagePostCount = ImagePost.objects.all().count()
		videoPostCount = VideoPost.objects.all().count()
		self.stdout.write('.....................................................')
		self.stdout.write('{image_count} image posts + {video_count} video posts g= {total} posts in total :) '.format(
			image_count=imagePostCount,
			video_count=videoPostCount,
			total=imagePostCount+videoPostCount)
		)
		self.stdout.write('.....................................................')