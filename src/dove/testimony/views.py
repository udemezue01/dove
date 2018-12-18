
from rest_framework import generics
from .serializers import TestimonySerializer
from .models import Testimony


from .permissions import IsOwnerOrReadOnly






class TestimonyAPIView(generics.ListCreateAPIView):
	lookup_field      =  'id'
	serializer_class  = TestimonySerializer
	

	def get_queryset(self):
		return Testimony.objects.all()


	def perform_create(self, serializer):
		serializer.save(user = self.request.user)




class TestimonyRUDView(generics.RetrieveUpdateDestroyAPIView):
	lookup_field		=	'id'
	serializer_class	=	TestimonySerializer


	def get_queryset(self):
		return Testimony.objects.all()


	def perform_update(self, serializer):
		serializer.save(user = self.request.user)


	def perform_delete(self, serializer):
		serializer.save(user = self.request.user)

		

	