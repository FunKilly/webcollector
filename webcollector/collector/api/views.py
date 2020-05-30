from rest_framework import generics, status

from collector.api.serializers import WebsiteParserSerializer
from collector.models import Website
from collector.tasks import parse_website


class WebsiteParserView(generics.ListCreateAPIView):
    model = Website
    serializer_class = WebsiteParserSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # task_id = self.perform_web_parsing(url=serializer.validated_data["url"])
        parse_website

        self.perform_create(serializer)
        website = serializer.instance

        return Response(website.id, status.HTTP_201_CREATED)

    def perform_web_parsing(self, url):
        task = parse_website.delay(url=url)

    def parse_website(url):
        from urllib.request import urlopen
        from bs4 import BeautifulSoup

        html = urlopen(url)
        BeautifulSoup(html, "lxml")
        import pdb

        pdb.set_trace()


class WebsiteView(generics.RetrieveApiView):
    serializer_class = WebsiteSerializer

    def get(self, request, *args, **kwargs):
        website = Website.objects.filter(task_id=self.kwargs["task_id"]).first()

        if not website:
            return Response("Website does not exist", status=status.HTTP_404_NOT_FOUND)
        else:
            # task_status =
            # data = {"email": user.email, "name": user.name, "role": user.role}
            # return Response(data, status=status.HTTP_200_OK)
            return Reponse("dupa")
