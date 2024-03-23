# Generated by Django 5.0.2 on 2024-03-19 18:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academics', '0008_remove_user_created_at_remove_user_created_at_at_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cities',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('abrev', models.CharField(max_length=20)),
                ('descrip', models.CharField(max_length=20)),
                ('ide_dept', models.IntegerField()),
                ('created_at', models.DateTimeField(default=datetime.datetime(2024, 3, 19, 13, 42, 13, 390258))),
                ('updated_at', models.DateTimeField(default=datetime.datetime(2024, 3, 19, 13, 42, 13, 390258))),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='person',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 3, 19, 13, 42, 13, 389221)),
        ),
        migrations.AlterField(
            model_name='person',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 3, 19, 13, 42, 13, 389221)),
        ),
        migrations.AlterField(
            model_name='user',
            name='cre_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 3, 19, 13, 42, 13, 327818)),
        ),
        migrations.AlterField(
            model_name='user',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 3, 19, 13, 42, 13, 327818)),
        ),
    ]
