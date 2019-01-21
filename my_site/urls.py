from django.contrib import admin
from django.urls import path, include

from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from .import views



urlpatterns = [    
    path('admin/', admin.site.urls),
    path('courses/', include('courses.urls')),
    path('', views.hello_world, name='home'),
]

urlpatterns += staticfiles_urlpatterns()