from django.db import models

# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

class Propietario(models.Model):
    cedula = models.PositiveIntegerField(primary_key=True)
    nombre = models.CharField(max_length=50, blank=True, null=True)
    s_nombre = models.CharField(max_length=50, blank=True, null=True)
    apellido = models.CharField(max_length=50, blank=True, null=True)
    s_apellido = models.CharField(max_length=50, blank=True, null=True)
    f_nacimiento = models.DateField(blank=True, null=True)
    contra = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        #managed = False
        db_table = 'Propietario'

class Motocicleta(models.Model):
    placa = models.CharField(primary_key=True, max_length=10)
    propietario_cedula = models.ForeignKey('Propietario', on_delete = models.CASCADE, db_column='Propietario_cedula')  # Field name made lowercase.
    modelo = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        #managed = False
        db_table = 'Motocicleta'


class Oficina(models.Model):
    idoficina = models.AutoField(db_column='idOficina', primary_key=True)  # Field name made lowercase.
    d_ubicacion = models.CharField(max_length=50, blank=True, null=True)
    nombre = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        #managed = False
        db_table = 'Oficina'


class Prueba(models.Model):
    idprueba = models.AutoField(db_column='idPrueba', primary_key=True)  # Field name made lowercase.
    oficina_idoficina = models.ForeignKey(Oficina, on_delete = models.CASCADE, db_column='Oficina_idOficina')  # Field name made lowercase.
    motocicleta_placa = models.ForeignKey(Motocicleta, on_delete = models.CASCADE, db_column='Motocicleta_placa')  # Field name made lowercase.
    resultado = models.CharField(max_length=50, blank=True, null=True)
    f_prueba = models.CharField(max_length=50, blank=True, null=True)
    p_dioxido = models.IntegerField(blank=True, null=True)

    class Meta:
        #managed = False
        db_table = 'Prueba'

