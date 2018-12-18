
from django.conf.urls import url

from .views import  (
        CommentAPIView,
		CommentRudView,

		)

app_name="comment"


urlpatterns = [

    url(r'^$', CommentAPIView.as_view(), name = 'comment-list'),
    
    url(r'^(?P<id>\w)/$', CommentRudView.as_view(), name = 'comment-detail'),
    
   
]