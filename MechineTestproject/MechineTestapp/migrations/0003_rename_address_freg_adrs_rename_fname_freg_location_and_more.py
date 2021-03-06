# Generated by Django 4.0 on 2022-04-07 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MechineTestapp', '0002_freg_address'),
    ]

    operations = [
        migrations.RenameField(
            model_name='freg',
            old_name='address',
            new_name='adrs',
        ),
        migrations.RenameField(
            model_name='freg',
            old_name='fname',
            new_name='location',
        ),
        migrations.RenameField(
            model_name='freg',
            old_name='gender',
            new_name='repassword',
        ),
        migrations.RenameField(
            model_name='freg',
            old_name='lname',
            new_name='uname',
        ),
        migrations.AddField(
            model_name='freg',
            name='img',
            field=models.ImageField(null=True, upload_to='image'),
        ),
        migrations.AddField(
            model_name='freg',
            name='number',
            field=models.IntegerField(null=True),
        ),
    ]
