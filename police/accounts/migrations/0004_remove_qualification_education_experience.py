# Generated by Django 3.0.8 on 2021-04-21 09:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_qualification_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='qualification',
            name='education_experience',
        ),
    ]
