#encoding: utf-8

from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.decorators import login_required
from django.db.models.aggregates import Sum
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.db.models.query_utils import Q

from django.urls.base import reverse_lazy

from contractors.forms import FormationItemForm, AchievementForm, EditContractorForm, EditContractorProfileForm, \
    CustomPasswordChangeForm
from contractors.models import Contractor, FormationItem, SportsAchievements, Session, BeneficiaryCategory, \
    BeneficiaryGroup, Intervention
from programs.views.subprogram_views import get_gender_resume


@login_required(login_url=reverse_lazy('login'))
def home(request):
    return redirect(reverse_lazy('contractor_home'))

def app_login(request):

    logout(request)
    username = password = ''
    error = False

    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        if username and password:
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect(reverse_lazy('home'))

                error = 'Usuario no activo'
            else:
                error = 'Credenciales no válidas'
        else:
            error = 'Usuario y contraseña requeridos'
    return render(request, 'login.html', {'error':error, 'site_user':username})


def app_logout(request):
    logout(request)
    return redirect(reverse_lazy('login'))


def restore_password(request):
    username = request.POST.get('user')
    error = False
    if username:
        try:
            user = User.objects.get(Q(username=username) | Q(email=username))
            password = User.objects.make_random_password()
            user.set_password(password)
            user.save()
            send_password_restore_mail(user, password)
            message = 'Se ha enviado un mensaje a su cuenta de correo con la información para restablecer la contraseña.'
            return render(request, 'login.html', {'message':message, 'restoring':True})
        finally:
            error = 'El usuario no existe'
            return render(request, 'login.html', {'message': error, 'restoring': True})

    else:
        error = 'Email o usuario requerido'
        return render(request, 'login.html', {'message': error, 'restoring': True})


@login_required(login_url='login')
def contractor_home(request):
    contractor = Contractor.objects.get(id=request.user.id)
    sessions = 0
    benefs = 0
    for interv in contractor.intervention_set.all():
        sessions += interv.session_set.all().count()
        
    return render(request, 'contractor_home.html', {'contractor':contractor, 'sessions':sessions, 'benefs':benefs})

@login_required(login_url='login')
def activity_report(request):

    if request.method == 'GET':
        contractor = Contractor.objects.get(id=request.user.id)
        intervs = contractor.intervention_set.all()

        return render(request, 'activity_report.html', {'intervs':intervs})
    if request.method == 'POST':
        intervention = Intervention.objects.get(id=request.POST.get('intervention'))
        session = Session(intervention=intervention, evidence=request.FILES.get('evidence'))
        session.save()

        for indexA in range(1,6):
            cat = BeneficiaryCategory(session = session,age_range=str(indexA))
            cat.save()

            print indexA

            groups = ['M','I','C','D','A']
            for index, val in enumerate(groups):

                print 'c' + str(indexA) + 'g' + str(index + 1) + 'f'
                print 'c' + str(indexA) + 'g' + str(index + 1) + 'm'

                group = BeneficiaryGroup(
                    category=cat,
                    group_name=val,
                    femenine_individuals=0,
                    masculine_individuals=0,
                )

                group.save()

        return redirect(reverse_lazy('contractor_home'))




        return render(request, 'activity_report.html', {'intervs': intervs})


@login_required(login_url='login')
def contractor_profile(request):
    contractor = Contractor.objects.get(id=request.user.id)
    return render(request, 'contractor_profile.html', {'contractor':contractor})



@login_required(login_url='login')
def edit_contractor_profile(request):

    pass_change = False
    if request.session.get('pass_changed'):
        pass_change = True
        del request.session['pass_changed']

    contractor = Contractor.objects.get(id=request.user.id)
    if request.method == 'GET':
        form = EditContractorProfileForm(instance=contractor)
        return render(request, 'contractor.html', {'contractor':contractor, 'pass':pass_change, 'form': form, 'editing': True})

    if request.method == 'POST':
        form = EditContractorProfileForm(request.POST, request.FILES, instance=contractor)

        if form.is_valid():
            contractor = form.save()
            return redirect(reverse_lazy('contractor_profile'))

        return render(request, 'contractor.html', {'contractor':contractor, 'form': form, 'pass':pass_change, 'editing':True})



@login_required(login_url='login')
def set_contractor_pass(request):
    if request.method == 'GET':
        form = CustomPasswordChangeForm(request.user, None)
        return render(request, 'set_password.html', {'form':form})

    if request.method == 'POST':
        form = CustomPasswordChangeForm(request.user,request.POST)
        if form.is_valid():
            user = form.save()
            return redirect(reverse_lazy('login'))
        return render(request, 'set_password.html', {'form':form})



@login_required(login_url='login')
def add_formation(request):

    contractor = Contractor.objects.get(appuser_ptr_id=request.user.id)
    if request.method == 'GET':
        form = FormationItemForm(initial={'trainer':contractor})
        return render(request, 'formation.html', {'contractor':contractor, 'form': form, 'formation':True})

    if request.method == 'POST':
        form = FormationItemForm(request.POST, request.FILES)

        if form.is_valid():
            formation_item = form.save()
            return redirect(reverse_lazy('contractor_profile'))

        return render(request, 'formation.html', {'contractor':contractor, 'form': form, 'formation':True})


@login_required(login_url='login')
def edit_formation(request, formation_id):

    contractor = Contractor.objects.get(appuser_ptr_id=request.user.id)
    formation = FormationItem.objects.get(id=formation_id)

    if request.method == 'GET':
        form = FormationItemForm(instance=formation, initial={'trainer':contractor})

        print form
        return render(request, 'formation.html', {'contractor':contractor, 'form': form, 'formation':True, 'editing':True})

    if request.method == 'POST':
        form = FormationItemForm(request.POST, request.FILES, instance=formation)

        if form.is_valid():
            formation_item = form.save()
            return redirect(reverse_lazy('contractor_profile'))

        return render(request, 'formation.html', {'contractor':contractor, 'form': form, 'formation':True, 'editing':True})

@login_required(login_url='login')
def delete_formation(request, formation_id):
    formation = FormationItem.objects.get(id=formation_id, trainer__id=request.user.id)
    formation.delete()
    return redirect(reverse_lazy('contractor_profile'))


@login_required(login_url='login')
def add_achievement(request):

    contractor = Contractor.objects.get(appuser_ptr_id=request.user.id)
    if request.method == 'GET':
        form = AchievementForm(initial={'trainer':contractor})
        return render(request, 'formation.html', {'contractor':contractor, 'form': form})

    if request.method == 'POST':
        form = AchievementForm(request.POST, request.FILES)

        if form.is_valid():
            achievement = form.save()
            return redirect(reverse_lazy('contractor_profile'))

        return render(request, 'formation.html', {'contractor':contractor, 'form': form})


@login_required(login_url='login')
def edit_achievement(request, achievement_id):

    contractor = Contractor.objects.get(appuser_ptr_id=request.user.id)
    achievement = SportsAchievements.objects.get(id=achievement_id)

    if request.method == 'GET':
        form = FormationItemForm(instance=achievement, initial={'trainer':contractor})
        return render(request, 'formation.html', {'contractor':contractor, 'form': form, 'formation':True, 'editing':True})

    if request.method == 'POST':
        form = FormationItemForm(request.POST, request.FILES, instance=achievement)

        if form.is_valid():
            achievement = form.save()
            return redirect(reverse_lazy('contractor_profile'))

        return render(request, 'formation.html', {'contractor':contractor, 'form': form, 'formation':True, 'editing':True})


@login_required(login_url='login')
def delete_achievement(request, achievement_id):
    achievement = SportsAchievements.objects.get(id=achievement_id, trainer__id=request.user.id)
    achievement.delete()
    return redirect(reverse_lazy('contractor_profile'))






def send_password_restore_mail(user, password):
    send_mail(
        subject=u'Recuperación de contraseña',
        message=u"""Se ha solicitado recuperar la contraseña para esta cuenta.
                   Se le ha generado un nueva contraseña de ingreso. Una vez iniciada la sesión recuerde cambiar su
                   contraseña desde la configuracion de su cuenta. La nueva contraseña es:"""+password+''.decode('utf-8'),
        html_message=u"""<p><b>Señor </b><br>"""+user.first_name+' '+user.last_name+u"""</b></p>
                    <p>Se ha solicitado recuperar la contraseña para su cuenta de administración en Ultra.<p>
                    <p>Se le ha generado un nueva contraseña de ingreso. Una vez iniciada la sesión, recuerde cambiar su
                    contraseña desde la configuracion de su cuenta.</p> La nueva contraseña es: <b>"""+password+'</b>'.decode('utf-8'),
        from_email='Ultra <ultra@indeportes.gov.co>',
        recipient_list=[user.email],
        fail_silently=False
    )


