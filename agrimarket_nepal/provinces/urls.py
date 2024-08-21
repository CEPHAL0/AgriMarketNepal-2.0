from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import ProvinceList
from django.contrib.auth.decorators import login_not_required
from django.utils.decorators import method_decorator

urlpatterns = [
    path("", login_not_required(ProvinceList.as_view()), name="province-list"),
]

urlpatterns = format_suffix_patterns(urlpatterns)
