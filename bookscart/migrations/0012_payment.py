# Generated by Django 4.2.2 on 2024-02-10 04:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookscart', '0011_delete_payment'),
    ]

    operations = [
        migrations.CreateModel(
            name='payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_on_card', models.CharField(max_length=100)),
                ('card_number', models.IntegerField()),
                ('exp_month', models.CharField(max_length=100)),
                ('exp_year', models.IntegerField()),
                ('cvv', models.IntegerField()),
                ('book_id', models.IntegerField()),
                ('total', models.IntegerField()),
            ],
        ),
    ]
