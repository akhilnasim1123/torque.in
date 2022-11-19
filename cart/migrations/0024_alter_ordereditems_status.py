# Generated by Django 4.1.2 on 2022-11-18 04:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0023_alter_ordereditems_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordereditems',
            name='status',
            field=models.CharField(choices=[('out for shipping', 'out for shipping'), ('completed', 'completed'), ('pending', 'pending')], default='pending', max_length=20),
        ),
    ]
