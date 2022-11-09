# Generated by Django 4.1.2 on 2022-11-03 11:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('proj', '0002_images_remove_category_category_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='subcategory',
        ),
        migrations.RemoveField(
            model_name='images',
            name='image2',
        ),
        migrations.AddField(
            model_name='images',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='proj.category'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='images',
            name='product',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='proj.product'),
            preserve_default=False,
        ),
    ]
