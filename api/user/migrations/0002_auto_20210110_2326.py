# Generated by Django 3.1.3 on 2021-01-10 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customeruser',
            name='gender',
        ),
        migrations.AlterField(
            model_name='customeruser',
            name='name',
            field=models.CharField(default='Anonymous', max_length=8),
        ),
    ]
