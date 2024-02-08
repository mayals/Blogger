from django.urls import path
from . import views


app_name = 'blog'

urlpatterns = [
    path('', views.home_view, name='home'),
    path('cat/<slug:catslug>/', views.home_filter_category, name='home-filter-category'),
    path('tag/<slug:tagslug>/', views.home_filter_tag, name='home-filter-tag'),
    # Post
    path('new-post/', views.post_create, name='new-post'),
    path('post-detail/<slug:post_slug>/', views.post_detail, name='post-detail'),
    path('post-update/<slug:slug>/', views.post_update, name= 'post-update'),
    path('post-delete-confirm/<slug:slug>/', views.post_delete_confirm, name ='post-delete-confirm'),
    path('post-like/<slug:post_slug>/', views.post_like_action, name='post-like'),
   
    path('google7a03622cb96e4f8f.html', views.google_verification_view),

    # Category
    # Tag
]
