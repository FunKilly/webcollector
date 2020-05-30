from rest_framework import generics, status

from webcollector.collector.api.serializers import WebsiteParserSerializer
from webcollector.collector.models import Website
from webcollector.collector.tasks import parse_website

from rest_framework.response import Response


class WebsiteParserView(generics.ListCreateAPIView):
    model = Website
    serializer_class = WebsiteParserSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # task_id = self.perform_web_parsing(url=serializer.validated_data["url"])
        self.parse_website(serializer.validated_data["url"])

        self.perform_create(serializer)
        website = serializer.instance

        return Response(website.id, status.HTTP_201_CREATED)

    def perform_web_parsing(self, url):
        task = parse_website.delay(url=url)

    def parse_website(self, url):
        from urllib.request import urlopen
        from bs4 import BeautifulSoup
        import urllib.request
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        html = urllib.request.urlopen(req).read()

        soup = BeautifulSoup(html, "lxml")
        import pdb

        pdb.set_trace()
        print(
            'smth'
        )


class WebsiteView(generics.RetrieveAPIView):
    def get(self, request, *args, **kwargs):
        task_id = self.kwargs.get("task_id")
        website = Website.objects.filter(task_id=task_id).first()

        if not website:
            return Response("Website does not exist", status=status.HTTP_404_NOT_FOUND)
        else:
            # task_status =
            # data = {"email": user.email, "name": user.name, "role": user.role}
            # return Response(data, status=status.HTTP_200_OK)
            return Reponse("dupa")
