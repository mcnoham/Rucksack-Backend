# Generated by Django 3.1.7 on 2021-05-03 01:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_auto_20210430_1009'),
    ]

    operations = [
        migrations.AddField(
            model_name='itinerary',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='upload/'),
        ),
        migrations.AddField(
            model_name='profile',
            name='profile_picture',
            field=models.ImageField(blank=True, null=True, upload_to='upload/'),
        ),
    ]