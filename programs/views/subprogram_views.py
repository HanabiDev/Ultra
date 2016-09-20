from athletes.views import permissions
from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, redirect
from django.urls.base import reverse_lazy

from programs.models import Program, Subprogram
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
        form = None
        if program_id:
            program = Program.objects.get(id=program_id)
            form = SubprogramForm(initial={'program': program})
        else:
            form = SubprogramForm()
        return render(request, 'subprogram.html', {'form': form})

    if request.method == 'POST':
        form = SubprogramForm(request.POST)

        if form.is_valid():
            new_subprogram = form.save()
            if program_id:
                return redirect(reverse_lazy('programs:view_program', kwargs={'program_id': str(program_id)}))

            return redirect(reverse_lazy('subprograms:view_subprogram', kwargs={'subprogram_id': str(new_subprogram.id)}))

        return render(request, 'subprogram.html', {'form': form})


@user_passes_test(permissions, login_url='login')
@login_required(login_url='login')
def view_subprogram(request, subprogram_id):
    subprogram = Subprogram.objects.get(id=subprogram_id)
    return render(request, 'subprogram_detail.html', {'subprogram': subprogram})


@user_passes_test(permissions, login_url='login')
@login_required(login_url='login')
def update_subprogram(request, subprogram_id):

    subprogram = Subprogram.objects.get(id=subprogram_id)
    if request.method == 'GET':
        form = SubprogramForm(instance=subprogram)
        return render(request, 'subprogram.html', {'subprogram':subprogram, 'form': form, 'editing': True})

    if request.method == 'POST':
        form = SubprogramForm(request.POST, request.FILES, instance=subprogram)

        if form.is_valid():
            subprogram = form.save()
            return redirect(reverse_lazy('subprograms:view_subprogram', kwargs={'subprogram_id': str(subprogram.id)}))

        return render(request, 'subprogram.html', {'subprogram':subprogram, 'form': form, 'editing':True})
