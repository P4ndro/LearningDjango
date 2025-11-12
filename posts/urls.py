from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.post_list, name='posts'),
    path('create/', views.create_post, name='create'),
    path('<slug:slug>/edit/', views.edit_post, name='edit'),
    path('<slug:slug>/delete/', views.delete_post, name='delete'),
    path('<slug:slug>/', views.post_page, name='page'),
]