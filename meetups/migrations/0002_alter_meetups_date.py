# Generated by Django 3.2.18 on 2023-04-10 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meetups', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meetups',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
    ]