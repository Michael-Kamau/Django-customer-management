# Generated by Django 4.2.11 on 2024-04-28 17:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_customerbusiness_building_floor_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customerbusiness',
            name='business_category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='base.businesscategory'),
        ),
    ]