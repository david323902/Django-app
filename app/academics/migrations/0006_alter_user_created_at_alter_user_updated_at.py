# Generated by Django 5.0.2 on 2024-03-15 21:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academics', '0005_alter_user_created_at_alter_user_updated_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 3, 15, 16, 43, 19, 604910)),
        ),
        migrations.AlterField(
            model_name='user',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 3, 15, 16, 43, 19, 604910)),
        ),
    ]