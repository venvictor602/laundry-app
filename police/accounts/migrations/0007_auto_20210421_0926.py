# Generated by Django 3.0.8 on 2021-04-21 08:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_contact'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='suubject',
            new_name='subject',
        ),
    ]
