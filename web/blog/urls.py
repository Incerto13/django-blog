from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from django.views.generic import TemplateView

from . import views

app_name = 'blog'
urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),  # POST only since Django 5.0
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('about/', TemplateView.as_view(template_name='blog/about.html'), name='about'),
    path('drafts/', views.draft_list, name='draft_list'),
    path('', views.post_list, name='post_list'),
]
