# Generated by Django 3.2.7 on 2021-11-13 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musicplayer', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='musicdb',
            name='song_category',
            field=models.CharField(default='Genaral', max_length=500),
        ),
    ]
