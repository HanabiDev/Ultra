#encoding: utf-8

from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.db.models.query_utils import Q

from django.urls.base import reverse_lazy

@login_required(login_url=reverse_lazy('login'))
def home(request):
    return redirect(reverse_lazy('contractors:list_contractors'))

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
                    return redirect(reverse_lazy('contractors:list_contractors'))

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

    else:
        error = 'Email o usuario requerido'
    return render_to_response('admin_login.html', {'rest_error':error, 'restoring':True}, context_instance=RequestContext(request))



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