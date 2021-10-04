from . import views
from django.urls import path

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('create-blog/', views.create_blog, name='create_blog'),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
    path('like/<int:pk>', views.like_view, name='like_post'),
    
]

