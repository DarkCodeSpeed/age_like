# Generated by Django 5.1.1 on 2024-09-13 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('age_likes', '0009_userage_device_info'),
    ]

    operations = [
        migrations.AddField(
            model_name='userage',
            name='username',
            field=models.CharField(default=0, max_length=100, unique=True),
            preserve_default=False,
        ),
    ]
