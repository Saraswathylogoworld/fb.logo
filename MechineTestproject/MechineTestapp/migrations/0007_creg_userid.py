# Generated by Django 4.0 on 2022-04-08 09:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('MechineTestapp', '0006_creg'),
    ]

    operations = [
        migrations.AddField(
            model_name='creg',
            name='userid',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='MechineTestapp.freg'),
        ),
    ]
