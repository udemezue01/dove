from django.db import models

from django.conf import settings



from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType


		
class StoryManger(models.Manager):

	def filter_by_instance(self, instance):
		user 			= instance.user	
		qs				= super(StoryManger, self).filter(user = user)
		return qs

	# def filter_by_story(self, instance):
	# 	target 			= ContentType.objects.get_for_model(instance.__class__)
	# 	obj_id 			=  instance.id
	# 	qs				= super(CommentManager, self).filter(target = target, object_id=obj_id)
	# 	return qs



class Story(models.Model):
	user 			= models.ForeignKey(settings.AUTH_USER_MODEL, on_delete= models.CASCADE )

	content 		= models.CharField(max_length = 4000)
	media 			= models.FileField(blank = True)
	created_at 		= models.DateTimeField(auto_now_add = True)

	objects 		= StoryManger()

	def __str__(self):
		return self.content


	def get_api_url(self):
		return reverse('story:story-detail', kwargs = {'id':self.id})

	@property
	def owner(self):
		return self.user

	@property
	def get_content_type(self):
		instance 		= self
		target 			= ContentType.objects.get_for_model(instance.__class__)
		return target

		