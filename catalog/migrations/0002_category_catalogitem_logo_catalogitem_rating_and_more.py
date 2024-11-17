# Generated by Django 5.1.3 on 2024-11-17 21:05

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('description', models.TextField(blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='catalogitem',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to='catalog_logos/'),
        ),
        migrations.AddField(
            model_name='catalogitem',
            name='rating',
            field=models.FloatField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)]),
        ),
        migrations.AddField(
            model_name='catalogitem',
            name='categories',
            field=models.ManyToManyField(blank=True, related_name='catalog_items', to='catalog.category'),
        ),
    ]
