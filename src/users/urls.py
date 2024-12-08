from django.urls import path

from users import views

app_name = "users"

urlpatterns = [
    path("welcome/", views.welcome, name="welcome"),
    path("", views.user_info, name="user_info"),
    path("registry/", views.registry, name="registry"),
]
