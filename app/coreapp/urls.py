from . import views
from django.urls import path

urlpatterns = [
    path('', views.BlogView.as_view(), name=''),
    path('', views.BlogView.as_view(), name='blog'),
    path('experience', views.CodeExpView.as_view(), name='experience'),
    path('posts/<slug:slug>/', views.BlogPost.as_view(), name='blog_post'),
]
