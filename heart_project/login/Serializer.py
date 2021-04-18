from rest_framework import serializers
from login.models import Register
from login.models import Login


class Loginserializer(serializers.ModelSerializer):

        class Meta:
            model=Register
            fields='__all__'


class Login2serializer(serializers.ModelSerializer):
    class Meta:
        model = Login
        fields = '__all__'