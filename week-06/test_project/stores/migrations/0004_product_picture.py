# Generated by Django 4.1.2 on 2023-02-10 01:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stores', '0003_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to='product_pictures/'),
        ),
    ]
