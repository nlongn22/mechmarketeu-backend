# Generated by Django 3.2.5 on 2021-07-28 22:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_alter_productmodel_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productmodel',
            name='description',
            field=models.TextField(default=''),
        ),
    ]
