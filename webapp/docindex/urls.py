from django.urls import path

from . import views


urlpatterns = [
    
    path('', views.index, name='index'),
    
    path('<int:study_plan_id>/', views.detail, name='detail' ),
    
    path('addnew/', views.addnew, name='addnew' ),
    
    path('<int:study_plan_id>/edit/', views.edit, name='edit'),
    
]