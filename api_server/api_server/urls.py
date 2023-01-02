from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("cafe/api/", include("cafe_api.urls")),
    path('admin/', admin.site.urls),
]
