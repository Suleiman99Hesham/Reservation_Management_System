# Generated by Django 4.0.2 on 2022-02-23 22:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0005_alter_appointment_rescheduled_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='client',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='backend.client'),
        ),
    ]
