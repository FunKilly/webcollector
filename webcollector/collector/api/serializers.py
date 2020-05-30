from rest_framework import serializers

from webcollector.collector.models import Website


class WebsiteParserSerializer(serializers.ModelSerializer):
    """ Base Serializer Class for listing News instances """

    class Meta:
        model = Website
        fields = ("url",)
