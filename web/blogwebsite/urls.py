"""blogwebsite URL configuration."""
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('sendmail/', include('sendmail.urls')),
    path('', include('blog.urls')),
]
