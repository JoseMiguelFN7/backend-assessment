# Generated by Django 5.1.4 on 2025-01-05 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vuelos', '0003_rename_id_agent_itinerary_agent'),
    ]

    operations = [
        migrations.AddField(
            model_name='airline',
            name='cod',
            field=models.CharField(default=None, max_length=5, null=True),
        ),
        migrations.AddField(
            model_name='leg',
            name='cod',
            field=models.CharField(default=None, max_length=5, null=True),
        ),
    ]
