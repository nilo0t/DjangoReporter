# Generated by Django 4.0.1 on 2022-01-17 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('use_Name', models.CharField(max_length=50)),
                ('Email', models.EmailField(max_length=50)),
                ('Mobile', models.IntegerField(max_length=15)),
                ('Roll', models.CharField(max_length=25)),
                ('create_Data', models.TimeField()),
            ],
        ),
    ]
