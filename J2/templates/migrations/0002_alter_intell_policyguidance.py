# Generated by Django 4.1.4 on 2023-04-25 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('J2', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='intell',
            name='policyguidance',
            field=models.CharField(choices=[('', 'Policy Guidance & Directive'), ('CENTCOM Theater Air and Missile Defense (TAMD) CONOPS', 'CENTCOM Theater Air and Missile Defense (TAMD) CONOPS'), ('CAPCO/ DoD Instruction', 'CAPCO/ DoD Instruction'), ('JCMB CONOPS', 'JCMB CONOPS'), ('Division Chief, J2 Guidance', 'Division Chief, J2 Guidance'), ('EJCMB CONOPS', 'EJCMB CONOPS'), ('SPECAT CONOPS', 'SPECAT CONOPS'), ('JEMB CONOPS', 'JEMB CONOPS'), ('ISR Improve-ment VTC CONOPS', 'ISR Improve-ment VTC CONOPS'), ('DIAM 58-12 ', 'DIAM 58-12 ')], max_length=210),
        ),
    ]
