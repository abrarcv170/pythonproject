from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from login.Serializer import Loginserializer
from login.Serializer import Login2serializer
from rest_framework.response import Response
from login.models import Register
from login.models import Login


# Create your views here.


class Loginview(APIView):
    def get(self, request):
        s = Register.objects.all()
        ser = Loginserializer(s, many=True)
        return Response(ser.data)

    def post(self, request):
        # ser=viewloginserializer(data=request.data)
        obj = Register()
        obj.gender = request.data["gender"]
        obj.dob = request.data["dob"]
        obj.password = request.data["password"]
        obj.user_name = request.data["user_name"]
        obj.email = request.data["email"]
        obj.phone_no = request.data["phone_no"]
        obj.save()

        ob = Login()
        ob.username = request.data["user_name"]
        ob.password = request.data["password"]
        ob.type ="user"
        ob.uid = obj.user_id
        ob.save()
        return HttpResponse("success")


class Loginv(APIView):
    def get(self,request):
        s=Login.objects.all()
        ser=Login2serializer(s,many=True)
        return Response(ser.data)


    def post(self,request):
        #ser=viewloginserializer(data=request.data)
        s = Login.objects.filter(username=request.data["user_name"],password=request.data["password"])
        ser = Login2serializer(s, many=True)
        return Response(ser.data)
