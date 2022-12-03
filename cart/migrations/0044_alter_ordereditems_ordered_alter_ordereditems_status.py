# Generated by Django 4.1.2 on 2022-12-03 11:31

import cart.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0043_alter_ordereditems_ordered_alter_ordereditems_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordereditems',
            name='ordered',
            field=cart.models.CustomDateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='ordereditems',
            name='status',
            field=models.CharField(choices=[('pending', 'pending'), ('delivered', 'delivered'), ('out for shipping', 'out for shipping'), ('completed', 'completed')], default='pending', max_length=20),
        ),
    ]
