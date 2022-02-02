from django.urls import path
from . import views

urlpatterns = [
    path('', views.StudentListView.as_view(), name='list'),
    path('<int:pk>/detail/', views.StudentDetailView.as_view(), name='detail'),
    path('new/', views.StudentCreateView.as_view(), name='create'),
    
    path('<int:pk>/update/', views.StudentUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', views.StudentDeleteView.as_view(), name='delete'),
]