# Generated by Django 3.2.5 on 2021-08-11 13:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20210811_1411'),
    ]

    operations = [
        migrations.RenameField(
            model_name='categorymodel',
            old_name='cables',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='categorymodel',
            name='deskmats',
        ),
        migrations.RemoveField(
            model_name='categorymodel',
            name='keyboards',
        ),
        migrations.RemoveField(
            model_name='categorymodel',
            name='keycaps',
        ),
        migrations.RemoveField(
            model_name='categorymodel',
            name='others',
        ),
        migrations.RemoveField(
            model_name='categorymodel',
            name='switches',
        ),
        migrations.AddField(
            model_name='productmodel',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='products.categorymodel'),
            preserve_default=False,
        ),
    ]
