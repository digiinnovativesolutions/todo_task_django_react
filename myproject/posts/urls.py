

from django.urls import path
from . import views

app_name = 'posts'  # This sets the URL namespace

urlpatterns = [
    path('list/', views.posts_list, name='list'),  # URL for listing posts
]

