# Generated by Django 3.0.2 on 2020-01-19 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wine', '0011_auto_20200119_1834'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wine',
            name='country',
            field=models.CharField(blank=True, choices=[('FR', 'Freshman'), ('SO', 'Sophomore'), ('JR', 'Junior'), ('SR', 'Senior'), ('GR', 'Graduate')], max_length=200),
        ),
    ]