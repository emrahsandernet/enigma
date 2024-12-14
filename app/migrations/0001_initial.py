# Generated by Django 4.2.17 on 2024-12-14 20:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='RegistryHelper',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key_hive', models.CharField(max_length=255)),
                ('key_version', models.CharField(max_length=255)),
                ('value_name', models.CharField(max_length=255)),
                ('value_type', models.CharField(max_length=255)),
                ('access_type', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='UserKey',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('key', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('oem_1', models.CharField(max_length=255)),
                ('oem_2', models.CharField(max_length=255)),
                ('oem_3', models.CharField(max_length=255)),
                ('timestamp1', models.CharField(max_length=255)),
                ('timestamp2', models.CharField(max_length=255)),
                ('timestamp3', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('status', models.BooleanField(default=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
