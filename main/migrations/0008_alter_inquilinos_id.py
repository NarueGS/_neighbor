# Generated by Django 4.0.1 on 2022-01-24 02:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_alter_inquilinos_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inquilinos',
            name='id',
            field=models.CharField(default='x5k18y4qnjkwzivv57lglc6798x5x307z4m8j880muy8lf01v5y0719n665320tu', editable=False, max_length=64, primary_key=True, serialize=False, unique=True),
        ),
    ]
