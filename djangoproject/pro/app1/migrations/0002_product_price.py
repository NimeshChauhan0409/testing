# Generated by Django 5.0.4 on 2024-04-18 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.IntegerField(default=2),
            preserve_default=False,
        ),
    ]
