from athletes.views import permissions
from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, redirect
from django.urls.base import reverse_lazy

from programs.models import Subprogram, Project
from programs.forms import ProjectForm

@login_required(login_url='login')
@user_passes_test(permissions, login_url='login')
def list_projects(request):
    projects = Project.objects.all()
    return render(request, 'projects_list.html', {'projects':projects})

@user_passes_test(permissions, login_url='login')
@login_required(login_url='login')
def create_project(request, subprogram_id=None):

    if request.method == 'GET':
        form = None
        if subprogram_id:
            subprogram = Subprogram.objects.get(id=subprogram_id)
            form = ProjectForm(initial={'subprogram': subprogram})
        else:
            form = ProjectForm()
        return render(request, 'project.html', {'form': form})

    if request.method == 'POST':
        form = ProjectForm(request.POST)

        if form.is_valid():
            new_project = form.save()
            if subprogram_id:
                return redirect(reverse_lazy('subprograms:view_subprogram', kwargs={'subprogram_id': str(subprogram_id)}))

            return redirect(reverse_lazy('projects:view_project', kwargs={'project_id': str(new_project.id)}))

        return render(request, 'project.html', {'form': form})


@user_passes_test(permissions, login_url='login')
@login_required(login_url='login')
def view_project(request, project_id):
    project = Project.objects.get(id=project_id)
    return render(request, 'project_detail.html', {'project': project})


@user_passes_test(permissions, login_url='login')
@login_required(login_url='login')
def update_project(request, project_id):

    project = Project.objects.get(id=project_id)
    if request.method == 'GET':
        form = ProjectForm(instance=project)
        return render(request, 'project.html', {'project':project, 'form': form, 'editing': True})

    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES, instance=project)

        if form.is_valid():
            project = form.save()
            return redirect(reverse_lazy('projects:view_project', kwargs={'project_id': str(project.id)}))

        return render(request, 'project.html', {'project':project, 'form': form, 'editing':True})
