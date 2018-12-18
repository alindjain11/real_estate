# Generated by Django 2.1.4 on 2018-12-17 08:45

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('sellers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImageField',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, upload_to='properties/%Y/%m/%d/')),
            ],
        ),
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('zipcode', models.CharField(max_length=20)),
                ('description', models.TextField(blank=True)),
                ('rice', models.IntegerField()),
                ('bedrooms', models.IntegerField()),
                ('bathrooms', models.DecimalField(decimal_places=1, max_digits=2)),
                ('garage', models.IntegerField(default=0)),
                ('sqft', models.IntegerField()),
                ('lot_size', models.DecimalField(decimal_places=1, max_digits=5)),
                ('photo_main', models.ImageField(upload_to='properties/%Y/%m/%d/')),
                ('photo_1', models.ImageField(blank=True, upload_to='properties/%Y/%m/%d/')),
                ('photo_2', models.ImageField(blank=True, upload_to='properties/%Y/%m/%d/')),
                ('photo_3', models.ImageField(blank=True, upload_to='properties/%Y/%m/%d/')),
                ('photo_4', models.ImageField(blank=True, upload_to='properties/%Y/%m/%d/')),
                ('photo_5', models.ImageField(blank=True, upload_to='properties/%Y/%m/%d/')),
                ('photo_6', models.ImageField(blank=True, upload_to='properties/%Y/%m/%d/')),
                ('is_published', models.BooleanField(default=True)),
                ('list_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='sellers.Seller')),
            ],
        ),
        migrations.AddField(
            model_name='imagefield',
            name='property',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='properties.Property'),
        ),
    ]