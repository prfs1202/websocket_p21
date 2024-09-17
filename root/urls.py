from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("chat/", include("apps.urls")),
    path("admin/", admin.site.urls),
]