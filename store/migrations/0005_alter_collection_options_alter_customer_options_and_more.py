# Generated by Django 4.0.2 on 2022-02-15 19:21

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_auto_20220212_1035'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='collection',
            options={'ordering': ['title']},
        ),
        migrations.AlterModelOptions(
            name='customer',
            options={'ordering': ['first_name', 'last_name']},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['title']},
        ),
        migrations.AlterField(
            model_name='product',
            name='inventory',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='product',
            name='promotions',
            field=models.ManyToManyField(blank=True, to='store.Promotion'),
        ),
        migrations.AlterField(
            model_name='product',
            name='unit_price',
            field=models.DecimalField(decimal_places=2, max_digits=6, validators=[django.core.validators.MinValueValidator(0)]),
        ),
    ]
