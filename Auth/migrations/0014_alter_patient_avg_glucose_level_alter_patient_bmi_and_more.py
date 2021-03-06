# Generated by Django 4.0.4 on 2022-06-28 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Auth', '0013_alter_patient_avg_glucose_level'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='avg_glucose_level',
            field=models.JSONField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='bmi',
            field=models.JSONField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='heart_disease',
            field=models.JSONField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='hypertension',
            field=models.JSONField(blank=True, null=True),
        ),
    ]
