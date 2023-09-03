# Generated by Django 4.2.2 on 2023-08-20 05:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('agri_iot', '0009_alter_userdetails_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='storedata',
            name='user',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='userdaycount',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
