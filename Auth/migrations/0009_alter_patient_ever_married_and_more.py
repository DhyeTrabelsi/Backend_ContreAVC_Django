# Generated by Django 4.0.4 on 2022-05-12 22:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Auth', '0008_adminstrateur'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='ever_married',
            field=models.CharField(blank=True, choices=[('Oui', 'Oui'), ('Non', 'Non')], default='Non', max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='smoking_status',
            field=models.CharField(blank=True, choices=[('ex', 'ex fumeur'), ('Actuellement', 'Actuellement fumeur'), ('Jamais', 'Jamais fumeur'), ('Inconnu', 'Inconnu')], default='Inconnu', max_length=12, null=True),
        ),
    ]