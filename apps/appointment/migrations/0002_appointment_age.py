# Generated by Django 4.2.15 on 2024-09-01 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='age',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
