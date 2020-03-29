# Generated by Django 3.0.3 on 2020-03-29 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wine', '0028_wine_foobar'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='wine',
            name='foobar',
        ),
        migrations.AddField(
            model_name='wine',
            name='dealer',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='wine',
            name='price',
            field=models.IntegerField(default=0),
        ),
    ]