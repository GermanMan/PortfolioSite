from django.shortcuts import render

from .models import Job

# Create your views here.
def home(request):
    jobs = Job.objects
    return render(request, 'jobs/home.html',{'jobs':jobs})

def projects(request):
    projects = Job.objects
    return render(request, 'jobs/projects.html',{'jobs':projects})