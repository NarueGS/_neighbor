# Generated by Django 4.0.1 on 2022-01-19 23:20

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_inquilinos_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inquilinos',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False),
        ),
    ]