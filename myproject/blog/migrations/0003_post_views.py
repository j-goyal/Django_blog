# Generated by Django 3.0.2 on 2020-06-06 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20200526_0048'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='views',
            field=models.IntegerField(default=0),
        ),
    ]
