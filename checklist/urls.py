
from . import views
from django.urls import path

urlpatterns = [
    path('', views.CheckListView.as_view(), name='checklist'),
    path('create/', views.create_item, name='create')
]