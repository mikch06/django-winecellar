# Generated by Django 3.0.2 on 2020-01-19 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wine', '0015_auto_20200119_1936'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wine',
            name='nmbrbottles',
            field=models.IntegerField(default=0),
        ),
    ]