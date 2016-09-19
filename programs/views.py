from athletes.views import permissions
from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, redirect
from django.urls.base import reverse_lazy
from programs.forms import ProgramForm
from programs.models import Program


@login_required(login_url='login')
@user_passes_test(permissions, login_url='login')
def list_programs(request):
    programs = Program.objects.all()
    return render(request, 'programs_list.html', {'programs':programs})

@user_passes_test(permissions, login_url='login')
@login_required(login_url='login')
def create_program(request):
    if request.method == 'GET':
        form = ProgramForm()
        return render(request, 'program.html', {'form': form})

    if request.method == 'POST':
        form = ProgramForm(request.POST, request.FILES)

        if form.is_valid():
            new_program = form.save()
            return redirect(reverse_lazy('programs:view_program', kwargs={'program_id': str(new_program.id)}))

        return render(request, 'program.html', {'form': form})


@user_passes_test(permissions, login_url='login')
@login_required(login_url='login')
def view_program(request, program_id):
    program = Program.objects.get(id=program_id)
    return render(request, 'program_detail.html', {'program': program})


@user_passes_test(permissions, login_url='login')
@login_required(login_url='login')
def update_program(request, program_id):

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


@user_passes_test(permissions, login_url='login')
@login_required(login_url='login')
def toggle_lock(request, user_id):
    contractor = Contractor.objects.get(id=user_id)
    contractor.is_active = not contractor.is_active
    contractor.save()
    return redirect(reverse_lazy('contractors:view_contractor', kwargs={'user_id': str(contractor.id)}))
