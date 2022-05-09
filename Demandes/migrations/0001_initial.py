# Generated by Django 4.0.4 on 2022-05-07 11:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Auth', '0007_remove_medecine_patients_patient_medecine'),
    ]

    operations = [
        migrations.CreateModel(
            name='Demande',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resultat', models.BooleanField(null=True)),
                ('medecine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Auth.medecine')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Auth.patient')),
            ],
        ),
    ]
