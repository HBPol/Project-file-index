from django.shortcuts import render

from fileindex.models import Project, Location, StudyPlan, Report, RelatedFile, LabBook

# Generate counts of some of the main objects
def index(request):
    num_projects = Project.objec.all().count()
    num_study_plans = StudyPlan.object.all().count()
    
    
    context = {
        'num_projects': num_projects,
        'num_study_plans': num_study_plans,
    }
    
    return render(request, 'index.html', context=context)
