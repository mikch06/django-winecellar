# Generated by Django 3.0.3 on 2020-03-29 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wine', '0029_auto_20200329_1707'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wine',
            name='dealer',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]