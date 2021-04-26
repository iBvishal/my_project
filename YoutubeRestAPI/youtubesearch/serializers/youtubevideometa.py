from rest_framework import serializers

from youtubesearch.models import YoutubeVideoMeta

class YoutubeVideoMetaSerializer(serializers.ModelSerializer):
    class Meta:
        model = YoutubeVideoMeta
        fields = "__all__"
