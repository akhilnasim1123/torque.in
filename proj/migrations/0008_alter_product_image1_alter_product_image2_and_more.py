# Generated by Django 4.1.2 on 2022-11-05 02:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proj', '0007_remove_product_pub_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image1',
            field=models.ImageField(upload_to='media/images'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image2',
            field=models.ImageField(upload_to='media/images'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image3',
            field=models.ImageField(upload_to='media/images'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image4',
            field=models.ImageField(upload_to='media/images'),
        ),
    ]
