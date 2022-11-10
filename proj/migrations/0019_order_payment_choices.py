# Generated by Django 4.1.2 on 2022-11-10 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proj', '0018_order_tracking_no_alter_orderitems_order_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='payment_choices',
            field=models.CharField(choices=[('razer pay', 'razer pay'), ('cash on delivery', 'cash on delivery'), ('paypal', 'paypal')], default='cash on delivery', max_length=100),
        ),
    ]
