from  django.conf.urls import url
from django.urls import path
from . import views

app_name ='urlapp'


urlpatterns = [
    path('', views.index, name='index'),
    path('other', views.other, name='other'),
    path('relative', views.relative, name='relative'),

]