from django.shortcuts import render, redirect
from .models import *
from .forms import ProjectForm
# Create your views here.

def projects(request):
    projects = Project.objects.all()
    context = {'projects':projects}
    return render(request,'projects/projects.html', context)


def project(request, pk):
    projects= Project.objects.get(id=pk)
    context = {'projects':projects}
    return render(request,'projects/single-project.html', context)

def createProject(request):
    form = ProjectForm()
    if request.method == "POST":
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid:
            form.save()
            return redirect('projects')
    context= {'form':form}
    return render(request,'projects/project_form.html', context)

def updateProject(request, pk):
    project = Project.objects.get(id=pk)
    form = ProjectForm(instance=project)
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid:
            form.save()
            return redirect('projects')
    context = {'project':project, 'form':form}
    return render(request,'projects/project_form.html', context)


def deleteProject(request, pk):
    object = Project.objects.get(id=pk)
    if request.method == "POST":
        object.delete()
        return redirect('projects')
    context = {'object':object}
    return render(request, 'projects/delete.html', context)
    

