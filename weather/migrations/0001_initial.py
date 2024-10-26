# Generated by Django 5.1.2 on 2024-10-26 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DailySummary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=100)),
                ('date', models.DateField()),
                ('average_temp', models.FloatField()),
                ('max_temp', models.FloatField()),
                ('min_temp', models.FloatField()),
                ('dominant_condition', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='WeatherData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=100)),
                ('main', models.CharField(max_length=100)),
                ('temp', models.FloatField()),
                ('feels_like', models.FloatField()),
                ('dt', models.DateTimeField()),
            ],
        ),
    ]