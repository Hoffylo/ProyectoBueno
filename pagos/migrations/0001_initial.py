# Generated by Django 5.1.2 on 2024-10-11 20:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('reservas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pago',
            fields=[
                ('id_pago', models.AutoField(primary_key=True, serialize=False)),
                ('monto_reserva', models.IntegerField()),
                ('fecha_pago', models.DateTimeField(auto_now_add=True)),
                ('tipo_comprobante', models.CharField(max_length=50)),
                ('comprobante_pago', models.CharField(max_length=100)),
                ('metodo_pago', models.CharField(max_length=50)),
                ('estado_pago', models.CharField(max_length=50)),
                ('id_reserva', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reservas.reserva')),
            ],
        ),
    ]
