# Generated by Django 2.0.6 on 2018-07-04 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_auto_20171017_1320'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bitpolluser',
            name='last_name',
            field=models.CharField(blank=True, max_length=150, verbose_name='last name'),
        ),
    ]
