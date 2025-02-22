# Generated by Django 5.1.1 on 2024-09-14 08:09

import django.db.models.deletion
import home.models
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Folder',
            fields=[
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to=home.models.get_uploaded_path)),
                ('folder', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.folder')),
            ],
        ),
    ]
