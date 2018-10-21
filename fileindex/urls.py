from django.urls import path
from fileindex import views

urlpatterns = [
    path('', views.index, name='index'),
]