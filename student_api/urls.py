import imp
from django.urls import path
from . import views

urlpatterns = [
    path('student/', views.StudentAPIView.as_view(), name='student-api'),
    path('student/<int:pk>/', views.StudentAPIView.as_view(), name='student-api'),
]