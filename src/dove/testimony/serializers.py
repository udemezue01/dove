from rest_framework.serializers import (
	ModelSerializer,
	SerializerMethodField,

	)
 
from .models import Testimony






class TestimonySerializer( ModelSerializer):
	

	user  =  SerializerMethodField()
	avatar = SerializerMethodField()
	class Meta:
		model 	=	Testimony
		fields	=	[
			'id',
			'user',
			'avatar',
	
			'content',
			'media',
			'created_at',
			
		]

	def get_user(self, obj):
		return str(obj.user.profile.username)

	def get_avatar(self,obj):
		try:
			avatar = str(obj.user.profile.avatar)
		except:
			avatar = None
		return avatar

