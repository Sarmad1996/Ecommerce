# Generated by Django 3.2.4 on 2021-07-07 10:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_contact'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='decc',
            new_name='desc',
        ),
    ]