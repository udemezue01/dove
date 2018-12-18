from rest_framework.serializers import (
	ModelSerializer,
	SerializerMethodField,

	)
 
from .models import Story


from comment.models import Comment
from comment.serializers import CommentSerializer



class StorySerializer( ModelSerializer):
	

	user  =  SerializerMethodField()
	avatar = SerializerMethodField()
	class Meta:
		model 	=	Story
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


class StoryDetailSerializer( ModelSerializer):
	

	user  =  SerializerMethodField()
	avatar = SerializerMethodField()
	comments  = SerializerMethodField()
	class Meta:
		model 	=	Story
		fields	=	[
			'id',
			'user',
			'avatar',
	
			'content',
			'media',
			'created_at',
			'comments',
			
		]	



	def get_user(self, obj):
		return str(obj.user.profile.username)

	def get_avatar(self,obj):
		try:
			avatar = str(obj.user.profile.avatar)
		except:
			avatar = None
		return avatar



	def get_comments(self, obj):
	
		target 		= obj.get_content_type
		object_id   = obj.id
		c_qs 		=  Comment.objects.filter_by_instance(obj)
		comments    = CommentSerializer(c_qs, many = True).data
		return comments


