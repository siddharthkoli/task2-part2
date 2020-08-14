from django.urls import path
from . import views

urlpatterns = [
    path("", views._login, name="_login"),
    path("signup", views.signup, name="signup"),
    path("logout", views._logout, name="_logout")
]