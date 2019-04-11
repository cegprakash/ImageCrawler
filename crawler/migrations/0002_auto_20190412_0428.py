# Generated by Django 2.2 on 2019-04-11 22:58

import crawler.utils.base_url_status
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crawler', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='baseurl',
            name='depth',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='baseurl',
            name='status',
            field=models.IntegerField(choices=[(0, 'unprocessed'), (1, 'processed'), (2, 'deleted')], default=crawler.utils.base_url_status.BaseUrlStatus(0)),
        ),
    ]
