from django.conf.urls import url,include
from . import views
app_name='energyapp'
urlpatterns = [
    url(r'^insert$',views.insert,name='insert'),
    url(r'^display$',views.display,name='display'),
    url(r'^home$',views.home,name='home')
    ]