from django.conf.urls import url
from login import views
urlpatterns = [

    url('^$',views.Loginview.as_view()),
    url('^login/',views.Loginv.as_view()),


]