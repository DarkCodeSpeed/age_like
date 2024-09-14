# Generated by Django 5.1.1 on 2024-09-13 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('age_likes', '0005_userage_f_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='userage',
            name='gender',
            field=models.CharField(blank=True, choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='userage',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='userage',
            name='f_name',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='userage',
            name='phone',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]
