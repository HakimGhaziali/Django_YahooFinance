# Generated by Django 4.1 on 2022-08-05 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Price', '0008_alter_data_ticker'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='ticker',
            field=models.CharField(max_length=50),
        ),
    ]
