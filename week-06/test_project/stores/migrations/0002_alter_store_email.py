# Generated by Django 4.1.2 on 2023-02-10 00:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stores', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='store',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
    ]
