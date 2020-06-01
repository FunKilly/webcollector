from rest_framework import generics, status
from rest_framework.response import Response

from webcollector.collector.api.serializers import WebsiteParserSerializer
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
        from celery.result import AsyncResult

        task = AsyncResult(str(task_id))
        return Response(task.status, status=status.HTTP_200_OK)
        # return Response(task_id, status=status.HTTP_200_OK)

        if not task_id:
            return Response("Website does not exist", status=status.HTTP_404_NOT_FOUND)
        else:
            # task_status =
            # data = {"email": user.email, "name": user.name, "role": user.role}
            # return Response(data, status=status.HTTP_200_OK)
            return Response("dupa")
