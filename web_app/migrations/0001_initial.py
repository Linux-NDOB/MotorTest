# Generated by Django 4.0.6 on 2022-07-16 15:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Motocicleta',
            fields=[
                ('placa', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('modelo', models.CharField(blank=True, max_length=10, null=True)),
                ('estado', models.CharField(blank=True, max_length=50, null=True)),
                ('categoria', models.CharField(blank=True, max_length=50, null=True)),
                ('f_fabricacion', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'Motocicleta',
            },
        ),
        migrations.CreateModel(
            name='Oficina',
            fields=[
                ('idoficina', models.AutoField(db_column='idOficina', primary_key=True, serialize=False)),
                ('d_ubicacion', models.PositiveIntegerField(blank=True, null=True)),
                ('nombre', models.PositiveIntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'Oficina',
            },
        ),
        migrations.CreateModel(
            name='Propietario',
            fields=[
                ('cedula', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(blank=True, max_length=50, null=True)),
                ('s_nombre', models.CharField(blank=True, max_length=50, null=True)),
                ('apellido', models.CharField(blank=True, max_length=50, null=True)),
                ('s_apellido', models.CharField(blank=True, max_length=50, null=True)),
                ('f_nacimiento', models.DateField(blank=True, null=True)),
            ],
            options={
                'db_table': 'Propietario',
            },
        ),
        migrations.CreateModel(
            name='Prueba',
            fields=[
                ('idprueba', models.AutoField(db_column='idPrueba', primary_key=True, serialize=False)),
                ('f_prueba', models.DateField(blank=True, null=True)),
                ('resultado', models.CharField(blank=True, max_length=10, null=True)),
                ('p_dioxido', models.FloatField(blank=True, null=True)),
                ('motocicleta_placa', models.ForeignKey(db_column='Motocicleta_placa', on_delete=django.db.models.deletion.DO_NOTHING, to='web_app.motocicleta')),
                ('oficina_idoficina', models.ForeignKey(db_column='Oficina_idOficina', on_delete=django.db.models.deletion.DO_NOTHING, to='web_app.oficina')),
            ],
            options={
                'db_table': 'Prueba',
            },
        ),
        migrations.AddField(
            model_name='motocicleta',
            name='propietario_cedula',
            field=models.ForeignKey(db_column='Propietario_cedula', on_delete=django.db.models.deletion.DO_NOTHING, to='web_app.propietario'),
        ),
    ]
