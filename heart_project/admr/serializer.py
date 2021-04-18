from rest_framework import serializers
from admr.models import AddMedicalRecord
class Admrserializer(serializers.ModelSerializer):

        class Meta:
            model=AddMedicalRecord
            fields='__all__'