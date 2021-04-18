from django.db import models


class AddMedicalRecord(models.Model):
    uid = models.IntegerField()
    date = models.CharField(max_length=50)
    result = models.CharField(max_length=100)
    accu = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'add_medical_record'


