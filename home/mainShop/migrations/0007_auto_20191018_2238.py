# Generated by Django 2.2.3 on 2019-10-18 17:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainShop', '0006_orderupdates'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Orders',
            new_name='Order',
        ),
        migrations.RenameModel(
            old_name='OrderUpdates',
            new_name='OrderUpdate',
        ),
    ]
