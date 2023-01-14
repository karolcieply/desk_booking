# Generated by Django 4.0.1 on 2023-01-14 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scheduler', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='session',
            name='lab_workstation',
            field=models.CharField(choices=[('Quantum Computing Workstation', 'Quantum Computing Workstation'), ('X-ray Diffraction Workstation', 'X-ray Diffraction Workstation'), ('Nuclear Magnetic Resonance Workstation', 'Nuclear Magnetic Resonance Workstation'), ('Particle Accelerator Workstation', 'Particle Accelerator Workstation')], default='A', max_length=40),
        ),
        migrations.AlterField(
            model_name='session',
            name='timeblock',
            field=models.CharField(choices=[('A', '8:00-9:00'), ('B', '9:00-10:00'), ('C', '10:00-11:00'), ('D', '11:00-12:00'), ('E', '12:00-13:00'), ('F', '13:00-14:00'), ('G', '14:00-15:00'), ('H', '15:00-16:00'), ('I', '16:00-17:00'), ('J', '17:00-18:00'), ('K', '18:00-19:00'), ('L', '19:00-20:00')], default='A', max_length=10),
        ),
    ]
