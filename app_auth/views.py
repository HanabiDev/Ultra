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
    CustomPasswordChangeForm, MemberForm
from contractors.models import Contractor, FormationItem, SportsAchievements, Session, BeneficiaryCategory, \
    BeneficiaryGroup, Intervention, Member
from programs.views.subprogram_views import get_gender_resume


def home(request):
    return redirect(reverse_lazy('site:home'))

@login_required(login_url=reverse_lazy('login'))
def admin_home(request):
    if request.user.is_staff or request.user.is_superuser:
        return redirect(reverse_lazy('programs:list_programs'))
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
                    return redirect(reverse_lazy('admin_home'))

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
        except Exception:
            error = 'Ha ocurrido un error'
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

        for session in interv.session_set.all():

            categories = session.beneficiarycategory_set.all()

            for cat in categories:
                Mt = cat.beneficiarygroup_set.all().aggregate(
                    Mtotal=Sum('masculine_individuals')
                )['Mtotal']

                Ft = cat.beneficiarygroup_set.all().aggregate(
                    Mtotal=Sum('femenine_individuals')
                )['Mtotal']

                benefs += Mt
                benefs += Ft
        
    return render(request, 'contractor_home.html', {'contractor':contractor, 'sessions':sessions, 'benefs':benefs})

@login_required(login_url='login')
def activity_report(request):

    if request.method == 'GET':
        contractor = Contractor.objects.get(id=request.user.id)
        intervs = contractor.intervention_set.all()

        return render(request, 'activity_report.html', {'intervs':intervs})
    if request.method == 'POST':

        c1 = [
            [request.POST.get('c1g1m'), request.POST.get('c1g1f')],
            [request.POST.get('c1g2m'), request.POST.get('c1g2f')],
            [request.POST.get('c1g3m'), request.POST.get('c1g3f')],
            [request.POST.get('c1g4m'), request.POST.get('c1g4f')],
            [request.POST.get('c1g5m'), request.POST.get('c1g5f')]
        ]
        c2 = [
            [request.POST.get('c2g1m'), request.POST.get('c2g1f')],
            [request.POST.get('c2g2m'), request.POST.get('c2g2f')],
            [request.POST.get('c2g3m'), request.POST.get('c2g3f')],
            [request.POST.get('c2g4m'), request.POST.get('c2g4f')],
            [request.POST.get('c2g5m'), request.POST.get('c2g5f')]
        ]

        c3 = [
            [request.POST.get('c3g1m'), request.POST.get('c3g1f')],
            [request.POST.get('c3g2m'), request.POST.get('c3g2f')],
            [request.POST.get('c3g3m'), request.POST.get('c3g3f')],
            [request.POST.get('c3g4m'), request.POST.get('c3g4f')],
            [request.POST.get('c3g5m'), request.POST.get('c3g5f')]
        ]

        c4 = [
            [request.POST.get('c4g1m'), request.POST.get('c4g1f')],
            [request.POST.get('c4g2m'), request.POST.get('c4g2f')],
            [request.POST.get('c4g3m'), request.POST.get('c4g3f')],
            [request.POST.get('c4g4m'), request.POST.get('c4g4f')],
            [request.POST.get('c4g5m'), request.POST.get('c4g5f')]
        ]

        c5 = [
            [request.POST.get('c5g1m'), request.POST.get('c5g1f')],
            [request.POST.get('c5g2m'), request.POST.get('c5g2f')],
            [request.POST.get('c5g3m'), request.POST.get('c5g3f')],
            [request.POST.get('c5g4m'), request.POST.get('c5g4f')],
            [request.POST.get('c5g5m'), request.POST.get('c5g5f')]
        ]

        c6 = [
            [request.POST.get('c6g1m'), request.POST.get('c6g1f')],
            [request.POST.get('c6g2m'), request.POST.get('c6g2f')],
            [request.POST.get('c6g3m'), request.POST.get('c6g3f')],
            [request.POST.get('c6g4m'), request.POST.get('c6g4f')],
            [request.POST.get('c6g5m'), request.POST.get('c6g5f')]
        ]

        cats = [c1,c2,c3,c4,c5,c6]

        intervention = Intervention.objects.get(id=request.POST.get('intervention'))
        session = Session(
            intervention=intervention,
            evidence=request.FILES.get('evidence'),
            plist=request.FILES.get('plist'),
            observations=request.POST.get('observations')
        )
        session.save()

        groups = ['M', 'C', 'I', 'D', 'A']
        for index, value in enumerate(cats):
            cat = BeneficiaryCategory(session = session,age_range=str((index+1)))
            cat.save()



            for i, item in enumerate(value):

                group = BeneficiaryGroup(
                    category=cat,
                    group_name=groups[i],
                    femenine_individuals=item[0],
                    masculine_individuals=item[1]
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



def contractor_groups(request):
    groups = Intervention.objects.filter(contractor_id=request.user.id)
    return render(request, 'groups_list.html', {'groups': groups})

def group_members(request, group_id):
    members = Intervention.objects.get(id=group_id).member_set.all()
    return render(request, 'members_list.html', {'members': members, 'group_id':group_id})

def add_member(request, group_id):
    interv = Intervention.objects.get(id=group_id)
    if request.method == 'GET':
        form = MemberForm(initial={'interv': interv})
        return render(request, 'member.html', {'interv': interv, 'form': form, 'group_id':group_id})

    if request.method == 'POST':
        form = MemberForm(request.POST, request.FILES)

        if form.is_valid():
            member = form.save()
            return redirect(reverse_lazy('group_members',kwargs={'group_id': str(group_id)}))

        return render(request, 'member.html', {'interv': interv, 'form': form, 'group_id':group_id})


def edit_member(request, group_id, member_id):
    interv = Intervention.objects.get(id=group_id)
    member = Member.objects.get(id=member_id)
    if request.method == 'GET':
        form = MemberForm(initial={'interv': interv}, instance=member)
        return render(request, 'member.html', {'interv': interv, 'form': form, 'editing':True, 'group_id':group_id})

    if request.method == 'POST':
        form = MemberForm(request.POST, request.FILES, instance=member)

        if form.is_valid():
            member = form.save()
            return redirect(reverse_lazy('group_members', kwargs={'group_id': str(group_id)}))

        return render(request, 'member.html', {'interv': interv, 'form': form, 'editing':True, 'group_id':group_id})


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


def load_report_form(request):
    contractor = Contractor.objects.get(id=request.user.id)
    intervs = contractor.intervention_set.all()

    return render(request, 'intervs.html', {'intervs': intervs})




def send_members(request, intervention_id):
    interv = Intervention.objects.get(id=intervention_id)
    members = interv.member_set.filter(active=True)
    if request.method == 'GET':
        return render(request, 'members.html', {'members': members})
    if request.method == 'POST':
        return redirect(reverse_lazy('home'))
