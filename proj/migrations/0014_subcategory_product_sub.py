# Generated by Django 4.1.2 on 2022-11-06 06:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('proj', '0013_delete_subcategory'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sub_name', models.CharField(max_length=50)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='proj.category')),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='sub',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='proj.subcategory'),
            preserve_default=False,
        ),
    ]