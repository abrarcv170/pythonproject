from django.conf.urls import url
from admr import views
urlpatterns = [
    url('^$',views.Admrview.as_view()),
    url(r'^android/',views.accviewrview.as_view()),

]