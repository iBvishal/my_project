# Generated by Django 2.2 on 2021-04-26 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('youtubesearch', '0001_initial'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='youtubevideometa',
            index=models.Index(fields=['title', 'description', '-PublishedOn'], name='youtubesear_title_30007a_idx'),
        ),
    ]
