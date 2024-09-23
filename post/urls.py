from . import views
from django.urls import path

urlpatterns = [
    path('posts/', views.PostView.as_view(), name='posts'),
]