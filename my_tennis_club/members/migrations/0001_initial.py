# Generated by Django 5.0.6 on 2024-05-28 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=225)),
                ('lastnamne', models.CharField(max_length=225)),
            ],
        ),
    ]
