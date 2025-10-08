
from . import views
from django.urls import path
from django.contrib.auth import views as auth_views


urlpatterns = [
    path("", views.index, name="index"),
    path("<str:room_name>/", views.room, name="room"),
]
