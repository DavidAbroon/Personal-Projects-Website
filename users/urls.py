from django.urls import path
from django.conf.urls import include
from . import views
from users.views import dashboard, register

urlpatterns = [
    path("dashboard/", views.dashboard, name="dashboard"),
    path("oauth/", include("social_django.urls")),
    path("register/", register, name="register"),
    path("accounts/", include("django.contrib.auth.urls")),
]
