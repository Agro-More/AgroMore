# Generated by Django 4.2.2 on 2023-08-09 17:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('agri_iot', '0004_remove_pricingmodel_planname_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pricingmodel',
            name='pri_slug',
        ),
        migrations.RemoveField(
            model_name='pricingmodel',
            name='pri_tag',
        ),
    ]
