# Generated by Django 5.0.3 on 2024-03-06 09:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookscart', '0014_payment'),
    ]

    operations = [
        migrations.DeleteModel(
            name='admin_addbooks',
        ),
        migrations.DeleteModel(
            name='buynow',
        ),
        migrations.DeleteModel(
            name='customer',
        ),
        migrations.DeleteModel(
            name='payment',
        ),
    ]
