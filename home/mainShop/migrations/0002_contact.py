# Generated by Django 2.2.3 on 2019-10-14 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainShop', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('msg_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('email', models.CharField(default='', max_length=90)),
                ('phone', models.CharField(default='', max_length=70)),
                ('desc', models.CharField(default='', max_length=600)),
            ],
        ),
    ]
