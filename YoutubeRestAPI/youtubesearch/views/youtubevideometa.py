from rest_framework import status, viewsets, mixins
from django_filters import rest_framework as filters
from youtubesearch.serializers import YoutubeVideoMetaSerializer
from youtubesearch.models import YoutubeVideoMeta

class CustomFilterSet(filters.FilterSet):
    title = filters.CharFilter(
        field_name="title", label="title of video", method="video_title"
    )

    def video_title(self, queryset, name, value):
        return queryset.filter(title__icontains=value)
    
    description = filters.CharFilter(
        field_name="description", label="description of video", method="video_description"
    )

    def video_description(self, queryset, name, value):
        return queryset.filter(description__icontains=value)

    class Meta:
	    model = YoutubeVideoMeta
	    fields = []

class YoutubeVideoMetaViewset(viewsets.ModelViewSet):
    queryset = YoutubeVideoMeta.objects.all().order_by('-PublishedOn')
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = CustomFilterSet
    serializer_class = YoutubeVideoMetaSerializer