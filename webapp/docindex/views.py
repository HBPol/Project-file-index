from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, Http404
from .models import StudyPlan
from django.template import loader
# Create your views here.
def index(request):
    study_plan_list = StudyPlan.objects.order_by('id')
    context = {
        'study_plan_list': study_plan_list,
    }
    return render(request, 'docindex/index.html', context)
    
def detail(request, study_plan_id):
    study_plan = get_object_or_404(StudyPlan, pk=study_plan_id)
    return render(request, 'docindex/detail.html', {'study_plan': study_plan})

def addnew(request):
    return HttpResponse("You are going to add a new study plan.")

def edit(request, study_plan_id):
    return HttpResponse("You are going to edit study plan number %s." %study_plan_id)
