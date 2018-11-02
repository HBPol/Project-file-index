from django.shortcuts import render

from fileindex.models import Project, Location, StudyPlan, Report, RelatedFile, LabBook
from django.views import generic
#from requests.api import request

def index(request):
    
    page_title = "R&D Electronic File Index"    
    num_projects = Project.objects.all().count()
    num_reports = Report.objects.all().count()
    num_study_plans = StudyPlan.objects.all().count()

    
    
    context = {
        'page_title': page_title,
        'num_projects': num_projects,
        'num_reports': num_reports,
        'num_study_plans': num_study_plans,
    }
    
    return render(request, 'fileindex/index.html', context=context)

# class ProjectListView(generic.ListView):
#    model = Project
# class ProjectDetailView(generic.DetailView):
#    model = Project

def project_list(request):
    project = Project.objects.all()
    context = {'project_list': project}
    return render(request, 'fileindex/project_list.html', context)

def project_detail(request, id):
    project = Project.objects.get(id=id)
    context = {'project_detail': project}
    return render(request, 'fileindex/project_detail.html', context)



class ReportListView(generic.ListView):
    model = Report   
class ReportDetailView(generic.DetailView):
    model = Report


class StudyPlanListView(generic.ListView):
    model = StudyPlan
class StudyPlanDetailView(generic.DetailView):
    model = StudyPlan
