# Generated by Django 4.0.4 on 2022-07-22 17:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Auth', '0016_patient_notifcation'),
    ]

    operations = [
        migrations.RenameField(
            model_name='patient',
            old_name='notifcation',
            new_name='notifier',
        ),
    ]