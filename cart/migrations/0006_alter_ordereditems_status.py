# Generated by Django 4.1.2 on 2022-11-22 04:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0005_alter_ordereditems_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordereditems',
            name='status',
            field=models.CharField(choices=[('pending', 'pending'), ('out for shipping', 'out for shipping'), ('completed', 'completed')], default='pending', max_length=20),
        ),
    ]