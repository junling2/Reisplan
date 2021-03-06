# Generated by Django 3.2.7 on 2021-09-09 19:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('itineraries', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='itinerary',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='itinerary',
            name='waypoint',
            field=models.ManyToManyField(to='itineraries.WayPoint'),
        ),
        migrations.AddField(
            model_name='foodstop',
            name='waypoint',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='itineraries.waypoint'),
        ),
        migrations.AddField(
            model_name='bed',
            name='waypoint',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='itineraries.waypoint'),
        ),
        migrations.AddField(
            model_name='attraction',
            name='waypoint',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='itineraries.waypoint'),
        ),
    ]
