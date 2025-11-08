from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LogoutView
from . import views  # import your homepage and other project views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homepage, name='homepage'),  # Example homepage
    path('about/', views.about, name='about'),  # Example about page
    
    # Include app-level URLs here; delegates routing responsibility to apps
    path('taskapp/', include('taskapp.urls', namespace='taskapp')),
    path('account/', include('account.urls')),
    path('analytics/', include('analytics.urls')),
    path('posts/', include('posts.urls', namespace='posts')),

    # Logout URL example
    path('logout/', LogoutView.as_view(), name='logout')
]
