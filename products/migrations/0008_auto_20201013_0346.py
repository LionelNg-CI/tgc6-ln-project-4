# Generated by Django 3.1 on 2020-10-13 03:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_auto_20201003_1633'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='pic',
            new_name='cover',
        ),
    ]
