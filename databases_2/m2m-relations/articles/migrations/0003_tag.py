# Generated by Django 2.2.10 on 2020-08-23 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_auto_20200822_1249'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Метка')),
                ('slug', models.SlugField(unique=True)),
            ],
            options={
                'db_table': 'tag',
            },
        ),
    ]
