# Generated by Django 3.0.8 on 2021-04-21 08:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_auto_20210421_0926'),
    ]

    operations = [
        migrations.RenameField(
            model_name='candidates',
            old_name='have_yo_beign_dependent_on_drugs_or_alcohol',
            new_name='have_you_beign_dependent_on_drugs_or_alcohol',
        ),
    ]
