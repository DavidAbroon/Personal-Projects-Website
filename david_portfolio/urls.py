from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('1013934asdkasdjasdk/', admin.site.urls),
    path("", include("projects.urls")),
    path("projects/", include("projects.urls")),
    path("blog/", include("blog.urls")),
    path("users/", include("users.urls")),
    path("accounts/", include("django.contrib.auth.urls")),    
]


