from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TaskViewSet
from . import views

app_name = 'taskapp'  # Required for namespaces

router = DefaultRouter()
router.register(r'tasks', TaskViewSet)

urlpatterns = [
   

    path('dashboard/', views.dashboard, name='dashboard'),
    path('task_list/', views.task_list, name='task_list'),
    path('task_detail/<int:pk>/', views.task_detail, name='task_detail'),
    path('task_create/', views.task_create, name='task_create'),
    path('task_delete/<int:pk>/', views.task_delete, name='task_delete'),
    path('task_tracking/', views.task_tracking, name='task_tracking'),
    
   
    path('timeline/', views.timeline_view, name='task_timeline'),
    path('task/update/<int:pk>/', views.task_update, name='task_update'),

    # Include DRF router URLs for API endpoints once!
    path('api/', include(router.urls)),
]
