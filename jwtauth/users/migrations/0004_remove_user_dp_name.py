# Generated by Django 3.2.6 on 2021-08-19 07:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_user_dp_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='dp_name',
        ),
    ]
