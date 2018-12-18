
from rest_framework import generics
from .serializers import LikeSerializer



from .permissions import IsOwnerOrReadOnly






class LikeAPIView(generics.ListCreateAPIView):
	lookup_field      =  'id'
	serializer_class  = LikeSerializer
	

	def get_queryset(self):
		return Like.objects.all()


	def perform_create(self, serializer):
		serializer.save(user = self.request.user)




class LikeRUDView(generics.RetrieveUpdateDestroyAPIView):
	lookup_field		=	'id'
	serializer_class	=	LikeSerializer


	def get_queryset(self):
		return Like.objects.all()


	def perform_update(self, serializer):
		serializer.save(user = self.request.user)


	def perform_delete(self, serializer):
		serializer.save(user = self.request.user)

		

	