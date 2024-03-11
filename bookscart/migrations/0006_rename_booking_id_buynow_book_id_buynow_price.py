# Generated by Django 4.2.2 on 2024-01-27 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookscart', '0005_buynow'),
    ]

    operations = [
        migrations.RenameField(
            model_name='buynow',
            old_name='booking_id',
            new_name='book_id',
        ),
        migrations.AddField(
            model_name='buynow',
            name='price',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]