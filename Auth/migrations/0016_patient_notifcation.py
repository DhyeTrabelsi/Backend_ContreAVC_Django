# Generated by Django 4.0.4 on 2022-07-22 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Auth', '0015_alter_patient_poids'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='notifcation',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
