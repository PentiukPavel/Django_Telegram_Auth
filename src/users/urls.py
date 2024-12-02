from django.urls import path

from users import views

app_name = "users"

urlpatterns = [
    path("welcome/", views.welcome, name="welcome"),
    path("me/", views.user_info, name="user_info"),
]
