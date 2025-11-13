from django.urls import path
from . import views

app_name = 'register'

urlpatterns = [
    path('', views.register, name='register'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('profile/<str:username>/', views.profile, name='profile'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),
    path('my-posts/', views.my_posts, name='my_posts'),
]

