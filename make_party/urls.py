from django.urls import path, include
from . import views

app_name='make_party'

urlpatterns = [
    path('', views.index, name='index'),
]