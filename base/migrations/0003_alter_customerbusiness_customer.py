# Generated by Django 4.2.11 on 2024-04-28 08:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_businesscategory_country_county_subcounty_ward_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customerbusiness',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='businesses', to='base.customer'),
        ),
    ]
