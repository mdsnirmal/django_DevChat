#urls file for full project
from django.contrib import admin
from django.urls import path, include 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('base.urls'))#redirecting to base.urls
]
 