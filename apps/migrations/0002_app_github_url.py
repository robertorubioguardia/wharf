# Generated by Django 2.0.2 on 2018-02-26 23:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='app',
            name='github_url',
            field=models.URLField(default=''),
            preserve_default=False,
        ),
    ]
