# Generated by Django 4.0.2 on 2022-05-03 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0009_remove_orderupdate_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='img',
            field=models.ImageField(default='', upload_to='media/shop/image'),
        ),
    ]
