# Generated by Django 4.2.2 on 2024-02-17 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookscart', '0013_delete_payment'),
    ]

    operations = [
        migrations.CreateModel(
            name='payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=100)),
                ('book_id', models.IntegerField()),
                ('total', models.IntegerField()),
                ('status', models.CharField(max_length=100)),
            ],
        ),
    ]
