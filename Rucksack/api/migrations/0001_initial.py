# Generated by Django 3.1.7 on 2021-04-09 17:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('user', models.OneToOneField(default=0, on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='auth.user')),
                ('description', models.TextField(default='', max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Itinerary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(default='', max_length=500)),
                ('budget', models.IntegerField(default=0)),
                ('duration_magnitude', models.IntegerField(default=0)),
                ('location_tag', models.CharField(default='', max_length=20)),
                ('transportation_tag', models.TextField(choices=[('Car', 'Car'), ('Train', 'Train'), ('Plane', 'Plane'), ('Motorcycle', 'Motorcycle'), ('Bicycle', 'Bicycle')], default='')),
                ('accommodation_tag', models.TextField(choices=[('Hotel', 'Hotel'), ('Hostel', 'Hostel'), ('Condo', 'Condo'), ('Campsite', 'Camp')], default='')),
                ('user', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]