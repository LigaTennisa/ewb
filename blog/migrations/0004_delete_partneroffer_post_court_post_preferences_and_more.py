# Generated by Django 5.0.2 on 2024-03-30 18:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_partneroffer_remove_post_court_remove_post_post_date_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='PartnerOffer',
        ),
        migrations.AddField(
            model_name='post',
            name='court',
            field=models.CharField(choices=[('Court A', 'Court A'), ('Court B', 'Court B'), ('Court C', 'Court C')], default='Court A', max_length=20),
        ),
        migrations.AddField(
            model_name='post',
            name='preferences',
            field=models.CharField(default='default_preference', max_length=20),
        ),
        migrations.AddField(
            model_name='post',
            name='training_date',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AddField(
            model_name='post',
            name='training_time',
            field=models.TimeField(default=datetime.time(0, 0)),
        ),
    ]
