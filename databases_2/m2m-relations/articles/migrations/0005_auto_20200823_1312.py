# Generated by Django 2.2.10 on 2020-08-23 10:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0004_auto_20200823_1253'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tag',
            options={'verbose_name': 'Метка', 'verbose_name_plural': 'Метки'},
        ),
    ]