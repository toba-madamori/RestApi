from django.urls import path
from .views import BlogListView, BlogDetailView, UserList, UserRetrieve
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('', BlogListView.as_view(), name='home'),
    path('post-detail/<int:pk>', BlogDetailView.as_view(), name='post-detail'),

    #User Endpoints
    path('user', UserList.as_view(), name='user'),
    path('user/<int:pk>', UserRetrieve.as_view(), name='user-detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)