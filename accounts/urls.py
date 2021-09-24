
from django.urls import path
from . import views


urlpatterns = [
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('profile/<str:user>', views.user_profile, name='profile'),
    path('logout/', views.logout_view, name='logout'),
]