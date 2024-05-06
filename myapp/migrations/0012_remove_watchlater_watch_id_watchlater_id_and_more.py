# Generated by Django 5.0 on 2024-03-07 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0011_watchlater_delete_listenlater'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='watchlater',
            name='watch_id',
        ),
        migrations.AddField(
            model_name='watchlater',
            name='id',
            field=models.AutoField(default=1, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='watchlater',
            name='video_id',
            field=models.CharField(max_length=255),
        ),
    ]
