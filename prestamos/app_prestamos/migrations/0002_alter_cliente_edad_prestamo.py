# Generated by Django 4.1.7 on 2023-03-11 16:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_prestamos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='Edad',
            field=models.IntegerField(),
        ),
        migrations.CreateModel(
            name='Prestamo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('monto', models.FloatField()),
                ('num_prestamo', models.IntegerField()),
                ('fecha', models.DateField(verbose_name='Fecha que se otorga el prestamo: ')),
                ('interes', models.IntegerField()),
                ('total_pago', models.IntegerField()),
                ('cliente_fk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_prestamos.cliente')),
            ],
        ),
    ]
