import uuid
from django.db import models
from django.utils.timezone import now

class YoutubeVideoMeta(models.Model):
    
    videoID = models.CharField(max_length=255)
    ChannelTitle = models.CharField(max_length=255)

    title = models.CharField(max_length=1023)
    description = models.TextField()
    thumbnailURL = models.URLField(max_length = 200)
    
    #when this record was published on Youtube
    PublishedOn = models.DateField(blank=True)
    
    #When this record was added to our db
    timeStamp = models.DateTimeField(auto_now_add=True, auto_now=False, blank=True)

    #index
    class Meta:
        indexes = [
            models.Index(fields=['title', 'description', '-PublishedOn']),
        ]

    #Show Title 
    def __str__(self):
        return self.title