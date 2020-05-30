
from collector.models import Website


class WebsiteParserSerializer(serializers.ModelSerializer):
    """ Base Serializer Class for listing News instances """

    class Meta(ExpertOpinionSerializer.Meta):
        model = Website
        fields = ("url",)
