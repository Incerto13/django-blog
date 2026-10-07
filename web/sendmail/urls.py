from django.urls import path

from . import views

app_name = 'sendmail'
urlpatterns = [
    path('email/', views.send_email, name='email'),
    path('success/', views.email_success, name='success'),
]
