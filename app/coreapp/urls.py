from . import views
from django.urls import path

urlpatterns = [
    path('', views.BlogView.as_view(), name=''),
    path('', views.BlogView.as_view(), name='blog'),
    path('experience', views.CodeExpView.as_view(), name='experience')
    #    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
]
