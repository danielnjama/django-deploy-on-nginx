# Generated by Django 4.2.13 on 2024-07-09 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_alter_customuser_activate_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='activate_code',
            field=models.PositiveIntegerField(default=906537),
        ),
    ]
