# Generated by Django 4.0.4 on 2022-06-28 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Auth', '0012_patient_heart_disease_patient_hypertension_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='avg_glucose_level',
            field=models.JSONField(blank=True, default='{0}', null=True),
        ),
    ]
