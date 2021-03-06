from rest_framework.serializers import (
	ModelSerializer,
	SerializerMethodField,

	)
 
from .models import Like






class LikeSerializer( ModelSerializer):
	

	user  =  SerializerMethodField()
	avatar = SerializerMethodField()
	class Meta:
		model 	=	Like
		fields	=	[
			'id',
			'user',
			'avatar',

			'target',
			'object_id',
			'likes_count',
			'liked',

			
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

