# Generated by Django 3.0.2 on 2020-05-12 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Wine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('winename', models.CharField(blank=True, max_length=200)),
                ('producer', models.CharField(blank=True, max_length=200)),
                ('grapes', models.CharField(blank=True, max_length=200)),
                ('year', models.IntegerField(blank=True, null=True)),
                ('country', models.CharField(choices=[('-', '-'), ('Australien', 'Australien'), ('Frankreich', 'Frankreich'), ('Deutschland', 'Deutschland'), ('Italien', 'Italien'), ('Österreich', 'Österreich'), ('Portugal', 'Portugal'), ('Schweiz', 'Schweiz'), ('Spanien', 'Spanien'), ('Südafrika', 'Südafrika'), ('USA', 'USA')], max_length=12)),
                ('region', models.CharField(blank=True, max_length=200)),
                ('purchase', models.DateField(blank=True)),
                ('price', models.CharField(blank=True, default=0, max_length=12)),
                ('dealer', models.CharField(blank=True, max_length=200)),
                ('drinkfrom', models.IntegerField(blank=True, null=True)),
                ('drinkto', models.IntegerField(blank=True, null=True)),
                ('nmbrbottles', models.IntegerField(default=0)),
                ('notes', models.CharField(blank=True, max_length=400)),
                ('editdate', models.DateField(auto_now=True)),
            ],
            options={
                'ordering': ['country', 'region', 'year'],
            },
        ),
    ]
