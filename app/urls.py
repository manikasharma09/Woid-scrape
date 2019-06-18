from django.conf.urls import url
from django.urls import path,re_path
from . import views
#from app.views import HomeView

app_name="app"

urlpatterns = [
       url(r'^home/$',views.home,name="home"),
]



 