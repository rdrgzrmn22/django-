# Generated by Django 4.1.3 on 2022-11-28 02:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('baseball', '0004_play'),
    ]

    operations = [
        migrations.AddField(
            model_name='club',
            name='team_pic',
            field=models.ImageField(blank=True, default='defaultimg.png', null=True, upload_to='', verbose_name='Team Image'),
        ),
    ]
