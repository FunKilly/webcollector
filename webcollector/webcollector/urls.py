from django.http import HttpResponse
from django.urls import include, path

urlpatterns = [
    path("", lambda r: HttpResponse()),
    path(
        "collector/", include(("webcollector.collector.urls", "admin"), namespace="admin")
    ),
]
