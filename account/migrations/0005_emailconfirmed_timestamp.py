# Generated by Django 2.0rc1 on 2018-01-05 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_auto_20180105_1548'),
    ]

    operations = [
        migrations.AddField(
            model_name='emailconfirmed',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]