# Generated by Django 4.2.5 on 2023-10-04 23:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='confirm',
            old_name='user_id',
            new_name='user',
        ),
    ]
