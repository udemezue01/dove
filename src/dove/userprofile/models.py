from django.db import models


from django.conf import settings
from django.db.models.signals import post_save
from rest_framework.reverse import reverse


from story.models import Story
from testimony.models import Testimony



class Profile (models.Model):
	

	user   		 		 = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
	

	username     		 = models.CharField(unique = True, max_length = 300)
	avatar       		 = models.FileField( blank = True , default = " {%static avatar.jpg%}" )
	bio   		  		 = models.CharField(max_length = 400, blank = True, verbose_name ='About')
	website				 = models.CharField(max_length = 5000, blank =True)
	phone 				 = models.IntegerField()

	country       		 = models.CharField(max_length = 1000)
	created_at 			 = models.DateTimeField(auto_now_add = True)



	def __str__(self):
		return str(self.user.full_name)  + '- '+'profile'

	def get_api_url(self):
		return reverse('profile:profile-detail', kwargs = {'username':self.username})


	@property
	def owner(self):
		return self.user

	@property
	def story(self):
		instance = self
		return Story.objects.filter_by_instance(instance)

	@property
	def testimony(self):
		instance = self
		return Testimony.objects.filter_by_instance(instance)




	# def create_profile(sender,**kwargs ):
	# 	if kwargs['created']:
	# 		user_profile=Profile.objects.create(user=kwargs['instance'])

	# post_save.connect(create_profile, sender=settings.AUTH_USER_MODEL)	

	



