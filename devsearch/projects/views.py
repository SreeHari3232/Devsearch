from django.shortcuts import render
from .models import *
# Create your views here.

def projects(request):
    projects = Project.objects.all()
    context = {'projects':projects}
    return render(request,'projects/projects.html', context)


def project(request, pk):
    projects= Project.objects.get(id=pk)
    context = {'projects':projects}
    return render(request,'projects/single-project.html', context)

