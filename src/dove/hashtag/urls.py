
from django.conf.urls import url

from .views import  (
        HashtagAPIVIew,
		HashtagRUDView,

		)

app_name="hashtag"


urlpatterns = [

    url(r'^$', HashtagAPIVIew.as_view(), name = 'hashtag-list'),
    
    url(r'^(?P<hashtag>\w)/$', HashtagRUDView.as_view(), name = 'hashtag-detail'),
    
   
]