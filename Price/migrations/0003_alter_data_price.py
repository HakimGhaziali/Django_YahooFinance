# Generated by Django 4.1 on 2022-08-06 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Price', '0002_alter_data_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
    ]
