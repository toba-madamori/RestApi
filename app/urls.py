from django.urls import path
from .views import blog_home, blogpost
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('', blog_home, name='home'),
    path('post-detail/<int:pk>', blogpost, name='post-detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)