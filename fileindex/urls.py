from django.urls import path
from fileindex import views

urlpatterns = [
    path('', views.index, name='index'),
    path('reports/', views.ReportListView.as_view(), name='reports'),
    path('projects/', views.ProjectListView.as_view(), name='projects'),
    path('study_plans/', views.StudyPlanListView.as_view(), name='study_plans'),
]