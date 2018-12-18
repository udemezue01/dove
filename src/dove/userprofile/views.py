
from rest_framework import generics
from .serializers import ProfileSerializer
from .models import Profile


from .permissions import IsOwnerOrReadOnly






class ProfileAPIView(generics.ListCreateAPIView):
	lookup_field      =  'username'
	serializer_class  = ProfileSerializer
	

	def get_queryset(self):
		return Profile.objects.all()


	def perform_create(self, serializer):
		serializer.save(user = self.request.user)




class ProfileRUDView(generics.RetrieveUpdateDestroyAPIView):
	lookup_field		=	'username'
	serializer_class	=	ProfileSerializer


	def get_queryset(self):
		return Profile.objects.all()


	def perform_update(self, serializer):
		serializer.save(user = self.request.user)


	def perform_delete(self, serializer):
		serializer.save(user = self.request.user)

		

	