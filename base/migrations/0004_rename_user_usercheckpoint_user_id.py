# Generated by Django 3.2.6 on 2024-03-15 20:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_auto_20240315_2048'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usercheckpoint',
            old_name='user',
            new_name='user_id',
        ),
    ]
