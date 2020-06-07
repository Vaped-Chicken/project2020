# Generated by Django 2.1.15 on 2020-06-07 00:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('make_party', '0002_changed_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='changed_photo',
            name='identificator',
            field=models.CharField(blank=True, max_length=150, verbose_name='identity'),
        ),
        migrations.AddField(
            model_name='photo',
            name='identificator',
            field=models.CharField(blank=True, max_length=150, verbose_name='identity'),
        ),
    ]