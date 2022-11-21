# Generated by Django 4.1.2 on 2022-11-20 14:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('proj', '0026_remove_orderitems_date_added'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderedItems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('out for shipping', 'out for shipping'), ('completed', 'completed'), ('pending', 'pending')], default='pending', max_length=20)),
                ('payment', models.CharField(max_length=120, null=True)),
                ('quantity', models.IntegerField(blank=True, null=True)),
                ('active', models.CharField(default='ordered', max_length=20)),
                ('price', models.CharField(blank=True, max_length=40, null=True)),
                ('payment_id', models.CharField(blank=True, max_length=100, null=True)),
                ('message', models.TextField(null=True)),
                ('tracking_no', models.CharField(max_length=150, null=True)),
                ('account', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('order', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='proj.order')),
                ('orderitems', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='proj.orderitems')),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='proj.product')),
                ('shippingaddress', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='proj.shippingaddress')),
            ],
        ),
    ]
