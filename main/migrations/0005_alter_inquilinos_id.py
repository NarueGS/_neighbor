# Generated by Django 4.0.1 on 2022-01-19 23:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_inquilinos_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inquilinos',
            name='id',
            field=models.CharField(default='4ce3fq71xy95np4rj53fws6ruz568wk5m484oh61a7593lnc4jgmss6530l870jw', editable=False, max_length=64, primary_key=True, serialize=False, unique=True),
        ),
    ]