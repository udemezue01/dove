from django.db import models

from django.conf import settings




class TestimonyManager(models.Manager):
	def filter_by_instance(self, instance):
		user 			= instance.user
		qs				= super(TestimonyManager, self).filter(user = user)
		return qs

class Testimony(models.Model):
	user 			= models.ForeignKey(settings.AUTH_USER_MODEL, on_delete= models.CASCADE  )

	content 		= models.CharField(max_length = 4000)
	media 			= models.FileField(blank = True)
	created_at 		= models.DateTimeField(auto_now_add = True)
	objects 		= TestimonyManager()

	def __str__(self):
		return str(self.user)

		