from django.urls import path
from .views import BlogListView, BlogDetailView
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('', BlogListView.as_view(), name='home'),
    path('post-detail/<int:pk>', BlogDetailView.as_view(), name='post-detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)