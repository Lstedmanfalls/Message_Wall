# Generated by Django 2.2 on 2021-08-12 23:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wall_app', '0003_auto_20210812_1635'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='message_id',
            new_name='message',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='user_id',
            new_name='user',
        ),
    ]
