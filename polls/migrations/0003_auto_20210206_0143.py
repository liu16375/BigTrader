# Generated by Django 3.1.6 on 2021-02-05 17:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_auto_20210206_0136'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='pub_update',
            new_name='pub_date',
        ),
    ]
