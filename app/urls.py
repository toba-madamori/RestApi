from django.urls import path
from .views import blog_home, blogpost

urlpatterns = [
    path('', blog_home, name='home'),
    path('post-detail/<int:pk>/', blogpost, name='post-detail'),
]