# Generated by Django 4.0 on 2022-04-08 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MechineTestapp', '0007_creg_userid'),
    ]

    operations = [
        migrations.AddField(
            model_name='creg',
            name='status',
            field=models.IntegerField(null=True),
        ),
    ]
