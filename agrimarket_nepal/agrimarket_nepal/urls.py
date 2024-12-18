from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import get_user_model
from rest_framework import routers
from django.conf.urls.static import static
from django.conf import settings

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path("users/", include("users.urls", namespace="users")),
    path("", include("consumables.urls", namespace="consumables")),
    path("admin", admin.site.urls),
]
