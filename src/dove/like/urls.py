
from django.conf.urls import url

from .views import  (
        LikeAPIView,
		LikeRUDView,

		)

app_name="like"


urlpatterns = [

    url(r'^$', LikeAPIView.as_view(), name = 'Like-list'),
    
    url(r'^(?P<id>\w)/$', LikeRUDView.as_view(), name = 'Like-detail'),
    
   
]