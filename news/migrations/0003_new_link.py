# Generated by Django 3.2.19 on 2023-07-11 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_auto_20230711_1456'),
    ]

    operations = [
        migrations.AddField(
            model_name='new',
            name='link',
            field=models.CharField(default=' ', max_length=200),
        ),
    ]