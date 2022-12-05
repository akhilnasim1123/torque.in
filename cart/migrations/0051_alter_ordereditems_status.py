# Generated by Django 4.1.2 on 2022-12-05 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0050_alter_ordereditems_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordereditems',
            name='status',
            field=models.CharField(choices=[('delivered', 'delivered'), ('out for shipping', 'out for shipping'), ('pending', 'pending'), ('completed', 'completed')], default='pending', max_length=20),
        ),
    ]