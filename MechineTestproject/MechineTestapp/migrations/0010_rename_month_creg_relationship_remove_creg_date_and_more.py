# Generated by Django 4.0 on 2022-04-08 11:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MechineTestapp', '0009_rename_status_creg_year_creg_month'),
    ]

    operations = [
        migrations.RenameField(
            model_name='creg',
            old_name='month',
            new_name='Relationship',
        ),
        migrations.RemoveField(
            model_name='creg',
            name='date',
        ),
        migrations.RemoveField(
            model_name='creg',
            name='year',
        ),
    ]
