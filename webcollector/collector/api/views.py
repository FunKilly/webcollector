from celery.result import AsyncResult
from rest_framework import generics, status
from rest_framework.response import Response

from webcollector.collector.api.serializers import WebsiteParserSerializer
from webcollector.collector.constants import CELERY_STATES
from webcollector.collector.models import Website
from webcollector.collector.tasks import parse_website


class WebsiteParserView(generics.ListCreateAPIView):
    model = Website
    serializer_class = WebsiteParserSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        task = parse_website.delay(url=serializer.validated_data["url"])

        context = {"task_id": task.id}
        return Response(context, status=status.HTTP_201_CREATED)


class WebsiteView(generics.RetrieveAPIView):
    def get(self, request, task_id, *args, **kwargs):
        task = AsyncResult(str(task_id))
        task_status = CELERY_STATES.get(task.state, "Current status was not included.")
        return Response(task_status, status=status.HTTP_200_OK)
