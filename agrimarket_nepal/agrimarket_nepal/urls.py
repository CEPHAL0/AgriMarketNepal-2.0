
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import get_user_model
from rest_framework import routers


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('users/', include('users.urls')),
    path('provinces/', include('provinces.urls')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('admin', admin.site.urls),
]
