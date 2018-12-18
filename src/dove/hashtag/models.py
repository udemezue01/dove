from django.db import models

from django.conf import settings
from story.models import Story

class Hashtag(models.Model):
	user 		= models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)

	story 		 = models.ForeignKey(Story , on_delete = models.CASCADE)
	hashtag 	 = models.CharField(max_length = 3000)

	created_at 	 = models.DateTimeField(auto_now_add = True)


	def __str__(self):
		return self.hashtag
