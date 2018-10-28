from django.urls import path
from fileindex import views

urlpatterns = [
    path('', views.index, name='index'),
    
    path('projects/', views.ProjectListView.as_view(), name='projects'),
    path('projects/<int:pk>', views.ProjectListView.as_view(), name='projects-detail'),
    
    path('reports/', views.ReportListView.as_view(), name='reports'),
    
    path('study_plans/', views.StudyPlanListView.as_view(), name='study-plans'),
]