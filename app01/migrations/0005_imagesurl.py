# Generated by Django 2.2.4 on 2019-11-20 03:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0004_auto_20191112_2124'),
    ]

    operations = [
        migrations.CreateModel(
            name='imagesUrl',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filter', models.CharField(max_length=64)),
                ('path', models.CharField(max_length=64)),
            ],
        ),
    ]
