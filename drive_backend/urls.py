from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('drive/', include('drive.urls')),
    path('admin/', admin.site.urls),
]
