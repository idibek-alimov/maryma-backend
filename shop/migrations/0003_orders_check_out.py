# Generated by Django 3.2.3 on 2021-06-19 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_orders'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='check_out',
            field=models.BooleanField(default=False),
        ),
    ]
