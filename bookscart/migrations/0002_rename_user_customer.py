# Generated by Django 4.2.2 on 2024-01-24 06:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookscart', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='user',
            new_name='customer',
        ),
    ]