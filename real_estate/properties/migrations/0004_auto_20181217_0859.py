# Generated by Django 2.1.4 on 2018-12-17 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0003_auto_20181217_0854'),
    ]

    operations = [
        migrations.RenameField(
            model_name='property',
            old_name='rice',
            new_name='price',
        ),
        migrations.AlterField(
            model_name='property',
            name='bathrooms',
            field=models.IntegerField(),
        ),
    ]