
from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('',views.home,name='home'),
    path('login/',views.log_in,name='log_in'),
    path('signin/',views.sign_in,name='sign_in'),
    path('logout/',views.logout,name='logout'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('profile/',views.profile,name='profile'),
    path('newpost/',views.post,name='post'),
    path('ram/', views.create_blog_post, name='create_blog_post'),
    path('blog/<slug:num>', views.blog, name='blog'),
    path('comment/<slug:id>', views.comment, name='comment'),
    path('like/<slug:id>/<slug:status>', views.likes, name='likes'),
    path('trash/<slug:num>', views.trash, name='trash'),
]
