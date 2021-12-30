# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class Todo(models.Model):
    task = models.CharField(max_length=80)
    is_complete = models.BooleanField(db_column='isComplete', default=False)  # Field name made lowercase.
    users = models.ForeignKey('users', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'todo'


class Users(models.Model):
    first_name = models.CharField(db_column='firstName', max_length=40)  # Field name made lowercase.
    last_name = models.CharField(db_column='lastName', max_length=60)  # Field name made lowercase.
    username = models.CharField(db_column='username', unique=True, max_length=100)
    password = models.CharField(db_column='password', max_length=100)
    is_active = models.BooleanField(db_column='isActive', default=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'users'
