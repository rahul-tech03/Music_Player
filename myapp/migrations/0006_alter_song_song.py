# Generated by Django 5.0 on 2024-02-24 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_alter_song_song'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='song',
            field=models.FileField(upload_to='documents'),
        ),
    ]
