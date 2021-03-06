# Generated by Django 3.1.5 on 2021-01-12 08:26

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=225)),
                ('email', models.CharField(max_length=225)),
                ('job', models.CharField(max_length=225)),
                ('address', models.JSONField()),
            ],
        ),
    ]
