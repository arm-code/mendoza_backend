# Generated by Django 4.2.7 on 2024-05-24 00:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mob_mendoza', '0003_order_deadline'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Generada', 'generada'), ('Entregada', 'entregada'), ('Completada', 'completada'), ('Cancelada', 'cancelada'), ('EnProceso', 'enproceso')], default='Generada', max_length=20),
        ),
    ]