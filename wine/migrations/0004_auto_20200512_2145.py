# Generated by Django 3.0.2 on 2020-05-12 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wine', '0003_auto_20200512_2116'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wine',
            name='winename',
            field=models.CharField(max_length=200),
        ),
    ]