from django.urls import path
from fileindex import views

urlpatterns = [
    path('', views.index, name='index'),
    
    #path('projects/', views.ProjectListView.as_view(), name='projects'),
    #path('projects/<int:pk>', views.ProjectDetailView.as_view(), name='project-detail'),
    
    path('projects/', views.project_list, name='projects'),
    path('projects/<int:id>', views.project_detail, name='project-detail'),
    
    path('reports/', views.ReportListView.as_view(), name='reports'),
    path('reports/<int:pk>', views.ReportDetailView.as_view(), name='report-detail'),
    
    path('study_plans/', views.StudyPlanListView.as_view(), name='study-plans'),
    path('study_plans/<int:pk>', views.StudyPlanDetailView.as_view(), name='studyplan-detail'),
]