from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.post_list, name='posts'),
    path('create/', views.create_post, name='create'),
    path('<slug:slug>/edit/', views.edit_post, name='edit'),
    path('<slug:slug>/delete/', views.delete_post, name='delete'),
    path('<slug:slug>/like/', views.like_post, name='like'),
    path('comment/<int:id>/delete/', views.delete_comment, name='delete_comment'),
    path('comment/<int:id>/edit/', views.edit_comment, name='edit_comment'),
    path('<slug:slug>/', views.post_page, name='page'),
]