# Generated by Django 3.2.9 on 2021-12-12 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musicplayer', '0015_remove_musicdb_song_language'),
    ]

    operations = [
        migrations.AlterField(
            model_name='musicdb',
            name='emotions',
            field=models.CharField(default='General', max_length=50000),
        ),
    ]
