# Generated by Django 3.1.3 on 2020-11-08 21:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ClassName',
            new_name='Customer',
        ),
    ]