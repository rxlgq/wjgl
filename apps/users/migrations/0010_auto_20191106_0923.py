# Generated by Django 2.2.3 on 2019-11-06 09:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_auto_20191105_1537'),
    ]

    operations = [
        migrations.RenameField(
            model_name='useroperatelog',
            old_name='userno',
            new_name='userno',
        ),
        migrations.RenameField(
            model_name='userprofile',
            old_name='userno',
            new_name='userno',
        ),
    ]
