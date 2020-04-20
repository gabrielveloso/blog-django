from django.urls import path
from .views import home, post
 

urlpatterns = [
    path('', home),
    path('posts/<int:post_id>', post)
]