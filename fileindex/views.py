from django.shortcuts import render

from fileindex.models import Project, Location, StudyPlan, Report, RelatedFile, LabBook

# Generate counts of some of the main objects
def index(request):
    num_projects = Project.objects.all().count()
    num_study_plans = StudyPlan.objects.all().count()
    
    
    context = {
        'num_projects': num_projects,
        'num_study_plans': num_study_plans,
    }
    
    return render(request, 'fileindex/index.html', context=context)
