# Generated by Django 3.1.3 on 2021-01-11 05:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20210110_2326'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customeruser',
            name='email',
            field=models.CharField(max_length=8, unique=True),
        ),
        migrations.AlterField(
            model_name='customeruser',
            name='phone',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
