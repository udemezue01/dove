
from django.conf.urls import url

from .views import  (
        ProfileAPIView,
		ProfileRUDView,

		)

app_name="profile"


urlpatterns = [

    url(r'^$', ProfileAPIView.as_view(), name = 'profile-list'),
    
    url(r'^(?P<username>\w+)/$', ProfileRUDView.as_view(), name = 'profile-detail'),
    
   
]