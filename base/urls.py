#urls for specific app
from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"), #path is blank, sending user to home
    path("room/", views.room, name="room"), # URLs trigger views
]