from athletes.views import permissions
from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, redirect
from django.urls.base import reverse_lazy

from contractors.models import Intervention
from polls.forms import PollForm, QuestionForm, OptionForm
from polls.models import Poll, Question, Option


@login_required(login_url='login')
@user_passes_test(permissions, login_url='login')
def list_polls(request):
    polls = Poll.objects.all()
    return render(request, 'polls_list.html', {'polls':polls})

@user_passes_test(permissions, login_url='login')
@login_required(login_url='login')
def create_poll(request):
    if request.method == 'GET':
        form = PollForm()
        return render(request, 'poll.html', {'form': form})

    if request.method == 'POST':
        form = PollForm(request.POST, request.FILES)

        if form.is_valid():
            new_poll = form.save()
            return redirect(reverse_lazy('polls:view_poll', kwargs={'poll_id': str(new_poll.id)}))

        return render(request, 'poll.html', {'form': form})


@user_passes_test(permissions, login_url='login')
@login_required(login_url='login')
def view_poll(request, poll_id):
    poll = Poll.objects.get(id=poll_id)
    return render(request, 'poll_detail.html', {'poll': poll})


@user_passes_test(permissions, login_url='login')
@login_required(login_url='login')
def update_poll(request, poll_id):

    poll = Poll.objects.get(id=poll_id)
    if request.method == 'GET':
        form = PollForm(instance=poll)
        return render(request, 'poll.html', {'poll':poll, 'form': form, 'editing': True})

    if request.method == 'POST':
        form = PollForm(request.POST, request.FILES, instance=poll)

        if form.is_valid():
            poll = form.save()
            return redirect(reverse_lazy('polls:view_poll', kwargs={'poll_id': str(poll.id)}))

        return render(request, 'poll.html', {'poll':poll, 'form': form, 'editing':True})


@user_passes_test(permissions, login_url='login')
@login_required(login_url='login')
def toggle_lock(request, poll_id):
    poll = Poll.objects.get(id=poll_id)
    poll.closed = not poll.closed
    poll.save()
    return redirect(reverse_lazy('polls:list_polls'))

@user_passes_test(permissions, login_url='login')
@login_required(login_url='login')
def create_question(request, poll_id):
    poll = Poll.objects.get(id=poll_id)
    if request.method == 'GET':
        form = QuestionForm(initial={'poll':poll})
        return render(request, 'question.html', {'form': form})

    if request.method == 'POST':
        form = QuestionForm(request.POST, request.FILES)

        if form.is_valid():
            new_question = form.save()
            return redirect(reverse_lazy('polls:view_question',
                                         kwargs={'poll_id': str(poll.id), 'question_id': str(new_question.id)}))

        return render(request, 'question.html', {'form': form})



@user_passes_test(permissions, login_url='login')
@login_required(login_url='login')
def view_question(request, poll_id, question_id):
    question = Question.objects.get(id=question_id)
    return render(request, 'question_detail.html', {'question': question})


@user_passes_test(permissions, login_url='login')
@login_required(login_url='login')
def update_question(request, poll_id, question_id):
    poll = Poll.objects.get(id=poll_id)
    question = Question.objects.get(id=question_id)
    if request.method == 'GET':
        form = QuestionForm(instance=question, initial={'poll':poll})
        return render(request, 'question.html', {'question':question, 'form': form, 'editing': True})

    if request.method == 'POST':
        form = QuestionForm(request.POST, request.FILES, instance=question)

        if form.is_valid():
            question = form.save()
            return redirect(reverse_lazy('polls:view_poll', kwargs={'poll_id': str(poll.id)}))

        return render(request, 'question.html', {'poll':poll, 'form': form, 'editing':True})


@user_passes_test(permissions, login_url='login')
@login_required(login_url='login')
def create_option(request, poll_id, question_id):
    poll = Poll.objects.get(id=poll_id)
    question = Question.objects.get(id=question_id)

    if request.method == 'GET':
        form = OptionForm(initial={'question':question})
        return render(request, 'option.html', {'form': form})

    if request.method == 'POST':
        form = OptionForm(request.POST, request.FILES)

        if form.is_valid():
            new_option = form.save()
            return redirect(reverse_lazy('polls:view_question',
                                         kwargs={'poll_id': str(poll.id), 'question_id': str(question.id)}))

        return render(request, 'option.html', {'form': form})


@user_passes_test(permissions, login_url='login')
@login_required(login_url='login')
def update_option(request, poll_id, question_id, option_id):
    poll = Poll.objects.get(id=poll_id)
    question = Question.objects.get(id=question_id)
    option = Option.objects.get(id=option_id)

    if request.method == 'GET':
        form = OptionForm(instance=option, initial={'question':question})
        return render(request, 'option.html', {'question':question, 'form': form, 'editing': True})

    if request.method == 'POST':
        form = OptionForm(request.POST, request.FILES, instance=option)

        if form.is_valid():
            option = form.save()
            return redirect(reverse_lazy('polls:view_question',
                                         kwargs={'poll_id': str(poll.id), 'question_id': str(question.id)}))

        return render(request, 'option.html', {'poll':poll, 'form': form, 'editing':True})