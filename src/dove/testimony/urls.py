
from django.conf.urls import url

from .views import  (
        TestimonyAPIView,
		TestimonyRUDView,

		)

app_name="testimony"


urlpatterns = [

    url(r'^$', TestimonyAPIView.as_view(), name = 'testimony-list'),
    
    url(r'^(?P<id>\w)/$', TestimonyRUDView.as_view(), name = 'testimony-detail'),
    
   
]