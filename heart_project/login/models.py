# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Register(models.Model):
    gender = models.CharField(max_length=10)
    dob = models.DateField(db_column='DOB')  # Field name made lowercase.
    password = models.CharField(max_length=40)
    user_name = models.CharField(max_length=100)
    user_id = models.AutoField(primary_key=True)
    email = models.CharField(max_length=200)
    phone_no = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'register'



class Login(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    type = models.CharField(max_length=40)
    uid = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'login'



