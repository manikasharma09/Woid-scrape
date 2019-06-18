from django.conf.urls import url, include
from django.contrib import admin
from django.urls import path,re_path
from scrape import views 
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url(r'^', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
    url(r'^$',views.login_redirect, name='login_redirect'),
    url(r'^app/',include('app.urls',namespace='app')),
    
    
]

    