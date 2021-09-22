from . import views
from django.urls import path

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('create-blog/', views.create_blog, name='create_blog'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
]