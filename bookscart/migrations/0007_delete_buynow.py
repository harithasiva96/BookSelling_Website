# Generated by Django 4.2.2 on 2024-01-27 09:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookscart', '0006_rename_booking_id_buynow_book_id_buynow_price'),
    ]

    operations = [
        migrations.DeleteModel(
            name='buynow',
        ),
    ]