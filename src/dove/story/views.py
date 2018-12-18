
from rest_framework import generics
from .serializers import (

	StorySerializer,
	StoryDetailSerializer,

	)
from .models import Story


from .permissions import IsOwnerOrReadOnly






class StoryAPIView(generics.ListCreateAPIView):
	lookup_field      =  'id'
	serializer_class  = StorySerializer
	

	def get_queryset(self):
		return Story.objects.all()


	def perform_create(self, serializer):
		serializer.save(user = self.request.user)




class StoryRUDView(generics.RetrieveUpdateDestroyAPIView):
	lookup_field		=	'id'
	serializer_class	=	StoryDetailSerializer


	def get_queryset(self):
		return Story.objects.all()


	def perform_update(self, serializer):
		serializer.save(user = self.request.user)


	def perform_delete(self, serializer):
		serializer.save(user = self.request.user)

		

	