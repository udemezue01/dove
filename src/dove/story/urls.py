
from django.conf.urls import url

from .views import  (
        StoryAPIView,
		StoryRUDView,

		)

app_name="story"


urlpatterns = [

    url(r'^$', StoryAPIView.as_view(), name = 'story-list'),
    
    url(r'^(?P<id>\w)/$', StoryRUDView.as_view(), name = 'story-detail'),
    
   
]