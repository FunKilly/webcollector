from django.urls import path

from webcollector.collector.api.views import WebsiteParserView, WebsiteView

urlpatterns = [
    path("parse-website", WebsiteParserView.as_view(), name="parse_website"),
    path("websites/<uuid:task_id>", WebsiteView.as_view(), name="website_list"),
]
