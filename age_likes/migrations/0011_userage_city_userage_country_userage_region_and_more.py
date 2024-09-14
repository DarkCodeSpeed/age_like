# Generated by Django 5.1.1 on 2024-09-14 05:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('age_likes', '0010_userage_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='userage',
            name='city',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='userage',
            name='country',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='userage',
            name='region',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='like',
            name='user_age',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='likes', to='age_likes.userage'),
        ),
    ]
