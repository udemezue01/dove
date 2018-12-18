from rest_framework.serializers import (
	ModelSerializer,
	SerializerMethodField,

	)
 
from .models import Profile


from story.serializers import StorySerializer
from story.models import Story


from testimony.serializers import TestimonySerializer
from testimony.models import Testimony



class ProfileSerializer( ModelSerializer):
	
	
	user  			=  SerializerMethodField()
	avatar 			= SerializerMethodField()
	story 		 	= SerializerMethodField()
	testimony 		= SerializerMethodField()
	class Meta:
		model 	=	Profile
		fields	=	[
			'id',
			'user',
			'avatar',

			'username',
			'bio',
	
			'country',
			'created_at',
			'story',
			'testimony',
			
		]


		

	def get_user(self, obj):
		return str(obj.user.profile.username)

	def validate_username(self, value):
		qs 	= Profile.objects.filter(username__iexact = value)
		if self.instance:
			qs = qs.exclude(id =self.instance.id)
		if qs.exists():
			raise serializers.ValidationError('Username already exist please pick another one')
		return value

	def get_avatar(self,obj):
		try:
			avatar = str(obj.user.profile.avatar)
		except:
			avatar = None
		return avatar


	def get_story(self, obj ):
		story  		= obj.story
		c_qs 		 =  Story.objects.filter_by_instance(obj)
		story   	 = StorySerializer(c_qs, many = True).data
		return story



	def get_testimony(self, obj ):
		testimony  			= 	obj.testimony
		c_qs 		 		=  	Testimony.objects.filter_by_instance(obj)
		testimony   	 	= 	TestimonySerializer(c_qs, many = True).data
		return testimony
		if testimony == none :
			raise ValidationError('no testimony yet')

		else:
			return testimony


	

