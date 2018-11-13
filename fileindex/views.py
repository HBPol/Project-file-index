from django.shortcuts import render

from fileindex.models import Project, Location, StudyPlan, Report, RelatedFile, LabBook
from django.views import generic

from django.shortcuts import redirect

#from requests.api import request

from fileindex.forms import StudyPlanForm
from audioop import reverse

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

# With generic list view:
# class ProjectListView(generic.ListView):
#    model = Project
def project_list(request):
    page_title = "Project list"
    project = Project.objects.all()
    context = {'page_title': page_title, 'project_list': project}
    return render(request, 'fileindex/project_list.html', context)

# With generic detail view:
# class ProjectDetailView(generic.DetailView):
#    model = Project
def project_detail(request, pk):
    project = Project.objects.get(id=pk)
    context = {'project_detail': project}
    return render(request, 'fileindex/project_detail.html', context)

def project_addnew(request):
    if request.method == "POST":
        project = Project(name=request.POST['name'], leader_id=request.POST['leader'])
        project.save()
        return redirect('/')
    else:
        return render(request, 'fileindex/project_addnew.html')



def project_update(request, pk):
    project = Project.objects.get(id=pk)
    context = {'project_detail': project}
    
    if request.method == "POST":
        project = Project.objects.get(id=pk)
        project.name = request.POST['name']
        project.leader_id = request.POST['leader']
        project.save()
        return redirect('/')
    else:
        return render(request, 'fileindex/project_update.html', context)


class ReportListView(generic.ListView):
    model = Report   
class ReportDetailView(generic.DetailView):
    model = Report


class StudyPlanListView(generic.ListView):
    model = StudyPlan
class StudyPlanDetailView(generic.DetailView):
    model = StudyPlan
    
def studyplan_update(request, pk):
    studyplan = StudyPlan.objects.get(id=pk)
    # If this is a POST request then process the form data
    if request.method == 'POST':
        # create a form instance and populate with data from the request
        studyplan_update_form = StudyPlanForm(request.POST)
        return HttpResponseRedirect(reverse('/'))
    else:
        studyplan_update_form = StudyPlanForm(initial={'title': title})
    
    contex = {
        'form': form,
        'studyplan': studyplan,
    }
    
    return render(request, 'fileindex/studyplan_update.html', context)
        
        
        
