from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from admr.serializer import Admrserializer
from rest_framework.response import Response
from admr.models import AddMedicalRecord
import datetime
from heart_project import settings
from pandas import read_excel
from pandas import read_csv
from sklearn.ensemble import RandomTreesEmbedding
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
# Create your views here.


class accviewrview(APIView):
    # def get(self, request):
    #     # s = AddMedicalRecord.objects.all()
    #     # ser = Admrserializer(s, many=True)
    #     # return Response(ser.data)
    #     pass

    def post(self, request):
        dspath = settings.BASE_DIR + settings.STATIC_URL + "heart.xlsx"
        data = read_excel(dspath, "heart")
        # data = read_csv("heart.csv")
        X = data.iloc[:, 0:13].values
        y = data.iloc[:, 13].values
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.3, random_state=0)
        hasher = RandomTreesEmbedding(n_estimators=10, random_state=0, max_depth=3)
        X_transformed = hasher.fit_transform(X_train)

        clf = LogisticRegression(random_state=0).fit(X_transformed,y_train)
        X_test=hasher.fit_transform(X_test)
        y_score = clf.predict(X_test)

        sc=accuracy_score(y_test, y_score)
        return HttpResponse(str(sc))

class Admrview(APIView):
    def get(self, request):
        s = AddMedicalRecord.objects.all()
        ser = Admrserializer(s, many=True)
        return Response(ser.data)

    def post(self, request):

        age = request.data["age"]
        sex = request.data["gen"]
        cp = request.data["c_pain"]
        trestbps = request.data["bp_lvl"]
        chol = request.data["choles"]
        fbs = request.data["bp_fast"]
        restecg = request.data["ecg"]
        talach = request.data["h_rate"]
        exang = request.data["i_exe"]
        oldpeak = request.data["d_exe"]
        slope = request.data["sd_seg"]
        ca = request.data["his"]
        thal = request.data["thal_scn"]

        dspath = settings.BASE_DIR + settings.STATIC_URL + "heart.xlsx"
        data = read_excel(dspath, "heart")
        # data = read_csv("heart.csv")
        X = data.iloc[:, 0:13].values
        y = data.iloc[:, 13].values

        hasher = RandomTreesEmbedding(n_estimators=10, random_state=0, max_depth=3)
        X_transformed = hasher.fit_transform(X)

        clf = LogisticRegression(random_state=0).fit(X_transformed, y)

        inp = age+"#"+sex+"#"+cp+"#"+trestbps+"#"+chol+"#"+fbs+"#"+restecg+"#"+talach+"#"+exang+"#"+oldpeak+"#"+slope+"#"+ca+"#"+thal
        import numpy as np
        inpa = np.fromstring(inp, dtype=np.float, sep='#')

        transformed_grid = hasher.transform([inpa])

        o = clf.predict(transformed_grid)
        print(o)



        obj = AddMedicalRecord()
        obj.uid = request.data["uid"]
        obj.date = datetime.date.today()
        # obj.date = "2020-02-02"
        if o == [1]:
            obj.result = "HEART PATIENT"
        if o == [0]:
            obj.result = "NO HEART DISEASE"


        dspath = settings.BASE_DIR + settings.STATIC_URL + "heart.xlsx"
        data = read_excel(dspath, "heart")
        # data = read_csv("heart.csv")
        X = data.iloc[:, 0:13].values
        y = data.iloc[:, 13].values
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.3, random_state=0)
        hasher = RandomTreesEmbedding(n_estimators=10, random_state=0, max_depth=3)
        X_transformed = hasher.fit_transform(X_train)

        clf = LogisticRegression(random_state=0).fit(X_transformed, y_train)
        X_test = hasher.fit_transform(X_test)
        y_score = clf.predict(X_test)

        sc = accuracy_score(y_test, y_score)

        obj.accu = sc*100
        obj.save()

        return HttpResponse("Success with Acc :"+ str(sc) )