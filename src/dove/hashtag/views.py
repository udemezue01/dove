
from rest_framework import generics
from .serializers import HashtagSerializer
from .models import Hashtag


from .permissions import IsOwnerOrReadOnly






class HashtagAPIVIew(generics.ListCreateAPIView):
	lookup_field      =  'hashtag'
	serializer_class  = HashtagSerializer
	

	def get_queryset(self):
		return Hashtag.objects.all()


	def perform_create(self, serializer):
		serializer.save(user = self.request.user)




class HashtagRUDView(generics.RetrieveUpdateDestroyAPIView):
	lookup_field		=	'hashtag'
	serializer_class	=	HashtagSerializer


	def get_queryset(self):
		return Hashtag.objects.all()


	def perform_update(self, serializer):
		serializer.save(user = self.request.user)


	def perform_delete(self, serializer):
		serializer.save(user = self.request.user)

		

	