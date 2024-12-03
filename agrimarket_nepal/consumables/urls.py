from django.urls import include, path

from consumables.views import ConsumablesCreateView, ConsumablesIndexView

app_name = "consumables"

urlpatterns = []
adminUrlPatterns = (
    [
        path("consumables", ConsumablesIndexView.as_view(), name="home"),
        path("consumables/create", ConsumablesCreateView.as_view(), name="create"),
    ],
    "admin",
)

urlpatterns += [path("admin/", include(adminUrlPatterns, namespace="admin"))]
