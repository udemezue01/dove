from django.db import models
from django.conf import settings

from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType




class Like(models.Model):
	user 		= models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)

	target 						= models.ForeignKey(ContentType, on_delete =  models.CASCADE)
	object_id 					= models.PositiveIntegerField()
	Content_object				= GenericForeignKey('target', 'object_id')

	likes_count 				= models.PositiveIntegerField(default = 0)
	liked      					=  models.BooleanField(default = False)

	created_at  				= models.DateTimeField(auto_now_add = True)

	def __str__(self):
		return str(self.user) + '- likes'