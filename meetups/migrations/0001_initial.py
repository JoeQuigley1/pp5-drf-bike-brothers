# Generated by Django 3.2.18 on 2023-05-26 20:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='MeetUps',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('content', models.TextField(blank=True)),
                ('date', models.DateField(null=True)),
                ('time', models.TimeField(null=True)),
                ('city', models.CharField(max_length=50)),
                ('venue', models.CharField(max_length=200)),
                ('bike_type', models.CharField(max_length=50)),
                ('spaces', models.IntegerField()),
                ('duration', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
