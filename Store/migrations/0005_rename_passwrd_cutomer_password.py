# Generated by Django 4.0.1 on 2022-01-14 09:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Store', '0004_cutomer'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cutomer',
            old_name='passwrd',
            new_name='password',
        ),
    ]
