from django.conf.urls import url
from  django.urls import path
from  . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('view', views.data_view, name='form-view')
]