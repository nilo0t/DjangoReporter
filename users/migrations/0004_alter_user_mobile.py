# Generated by Django 4.0.1 on 2022-01-17 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_user_create_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='Mobile',
            field=models.CharField(max_length=15),
        ),
    ]
