# Generated by Django 4.2.7 on 2024-05-22 17:29

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('mob_mendoza', '0002_address_rename_id_customer_cart_customer_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='deadline',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]