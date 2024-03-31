# Generated by Django 5.0.2 on 2024-03-30 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_court_post_post_date_post_post_time'),
    ]

    operations = [
        migrations.CreateModel(
            name='PartnerOffer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('contact_email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.RemoveField(
            model_name='post',
            name='court',
        ),
        migrations.RemoveField(
            model_name='post',
            name='post_date',
        ),
        migrations.RemoveField(
            model_name='post',
            name='post_time',
        ),
    ]