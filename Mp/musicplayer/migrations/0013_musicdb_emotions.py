# Generated by Django 3.2.9 on 2021-11-21 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musicplayer', '0012_auto_20211120_2024'),
    ]

    operations = [
        migrations.AddField(
            model_name='musicdb',
            name='emotions',
            field=models.CharField(default='General', max_length=500),
        ),
    ]
