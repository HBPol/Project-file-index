from django.shortcuts import render
from django.http import HttpResponse
from .models import StudyPlan
# Create your views here.
def index(request):
    #return HttpResponse("This is the list of study plans.")
    study_plan_list = StudyPlan.objects.order_by('id')
    output = ', '.join([sp.title for sp in study_plan_list])
    return HttpResponse(output)
    
def detail(request, study_plan_id):
    return HttpResponse("You are looking at study plan number %s." %study_plan_id)

def addnew(request):
    return HttpResponse("You are going to add a new study plan.")

def edit(request, study_plan_id):
    return HttpResponse("You are going to edit study plan number %s." %study_plan_id)
