# Generated by Django 3.0.8 on 2022-02-21 01:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20220220_1948'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='total_expenditure_today',
            field=models.CharField(default='', max_length=200),
        ),
    ]
