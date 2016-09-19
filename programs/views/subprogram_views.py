from athletes.views import permissions
from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, redirect
from django.urls.base import reverse_lazy

from programs.models import Subprogram
from programs.forms import SubprogramForm

@login_required(login_url='login')
@user_passes_test(permissions, login_url='login')
def list_subprograms(request):
    subprograms = Subprogram.objects.all()
    return render(request, 'subprograms_list.html', {'subprograms':subprograms})

@user_passes_test(permissions, login_url='login')
@login_required(login_url='login')
def create_subprogram(request, program_id=None):
    if request.method == 'GET':
        form = SubprogramForm()
        return render(request, 'subprogram.html', {'form': form})

    if request.method == 'POST':
        form = SubprogramForm(request.POST, request.FILES)

        if form.is_valid():
            new_program = form.save()
            return redirect(reverse_lazy('programs:view_program', kwargs={'program_id': str(new_program.id)}))

        return render(request, 'subprogram.html', {'form': form})


@user_passes_test(permissions, login_url='login')
@login_required(login_url='login')
def view_subprogram(request, program_id):
    program = Program.objects.get(id=program_id)
    return render(request, 'program_detail.html', {'program': program})


@user_passes_test(permissions, login_url='login')
@login_required(login_url='login')
def update_subprogram(request, program_id):

    program = Program.objects.get(id=program_id)
    if request.method == 'GET':
        form = ProgramForm(instance=program)
        return render(request, 'program.html', {'program':program, 'form': form, 'editing': True})

    if request.method == 'POST':
        form = ProgramForm(request.POST, request.FILES, instance=program)

        if form.is_valid():
            program = form.save()
            return redirect(reverse_lazy('programs:view_program', kwargs={'program_id': str(program.id)}))

        return render(request, 'program.html', {'program':program, 'form': form, 'editing':True})
