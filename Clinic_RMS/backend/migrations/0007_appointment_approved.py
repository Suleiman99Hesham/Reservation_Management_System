# Generated by Django 4.0.2 on 2022-02-24 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0006_alter_appointment_client'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='approved',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]