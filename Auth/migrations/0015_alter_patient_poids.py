# Generated by Django 4.0.4 on 2022-06-28 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Auth', '0014_alter_patient_avg_glucose_level_alter_patient_bmi_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='poids',
            field=models.JSONField(blank=True, default=0, null=True),
        ),
    ]