from rest_framework import routers
from django.urls import include, path

from youtubesearch.views import YoutubeVideoMetaViewset

router = routers.DefaultRouter()
router.register(r'youtubevideometa', YoutubeVideoMetaViewset)

urlpatterns = [
    path('', include(router.urls)),
]