# Generated by Django 3.1.3 on 2021-01-11 05:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_auto_20210111_1113'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customeruser',
            name='email',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]
