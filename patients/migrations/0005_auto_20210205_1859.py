# Generated by Django 3.1.5 on 2021-02-05 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0004_auto_20210203_1539'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='phone_number',
            field=models.BigIntegerField(blank=True, default=234),
        ),
    ]
