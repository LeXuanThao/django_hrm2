# Generated by Django 4.2.20 on 2025-04-19 05:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SpecialDate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(unique=True)),
                ('is_holiday', models.BooleanField(default=False)),
                ('description', models.CharField(max_length=255)),
            ],
        ),
    ]
