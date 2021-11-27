# Generated by Django 3.2.7 on 2021-11-14 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musicplayer', '0007_auto_20211114_1638'),
    ]

    operations = [
        migrations.AlterField(
            model_name='musicdb',
            name='image',
            field=models.ImageField(default='musicplayer/images', upload_to='musicplayer/images'),
        ),
        migrations.AlterField(
            model_name='musicdb',
            name='song',
            field=models.FileField(default='musicplayer/songs', upload_to='musicplayer/songs'),
        ),
    ]