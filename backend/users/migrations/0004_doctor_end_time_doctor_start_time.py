# Generated by Django 4.2.7 on 2023-12-19 21:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_rename_first_name_doctor_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='end_time',
            field=models.TimeField(null=True),
        ),
        migrations.AddField(
            model_name='doctor',
            name='start_time',
            field=models.TimeField(null=True),
        ),
    ]
