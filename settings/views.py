from django.shortcuts import render, redirect
from athletes.models import Sport, League, Club
from django.urls.base import reverse_lazy

from settings.forms import SportForm, LeagueForm, ClubForm

def home(request):
	return render(request, "settings.html")


def sports_index(request):
	sports = Sport.objects.all()
	return render(request, "sports.html", {'sports':sports})


def create_sport(request):

	if request.method == 'GET':
		form = SportForm()
		return render(request, 'sport.html', {'form': form})

	if request.method == 'POST':
		form = SportForm(request.POST)
		
		if form.is_valid():
			new_sport = form.save()
			return redirect(reverse_lazy('settings:view_sport', kwargs={'sport_id': str(new_sport.id)}))
			#return redirect(reverse_lazy('athletes:view', kwargs={'user_id': str(new_athlete.id)}))

		return render(request, 'sport.html', {'form': form})


def edit_sport(request, sport_id):
	sport = Sport.objects.get(id=sport_id)

	if request.method == 'GET':
		form = SportForm(instance=sport)
		return render(request, 'sport.html', {'form': form, 'editing':True, 'sport':sport})

	if request.method == 'POST':
		form = SportForm(request.POST, instance=sport)
		
		if form.is_valid():
			sport = form.save()
			return redirect(reverse_lazy('settings:view_sport', kwargs={'sport_id': str(sport.id)}))
			#return redirect(reverse_lazy('athletes:view', kwargs={'user_id': str(new_athlete.id)}))

		return render(request, 'sport.html', {'form': form, 'editing':True, 'sport':sport})


def view_sport(request, sport_id):
	sport = Sport.objects.get(id=sport_id)
	return render(request, 'sport_detail.html', {'sport': sport})


def delete_sport(request, sport_id):
	sport = Sport.objects.get(id=sport_id)
	sport.delete()

	return redirect(reverse_lazy('settings:sports_index'))



def leagues_index(request):
	leagues = League.objects.all()
	return render(request, "leagues.html", {'leagues':leagues})


def create_league(request, sport_id=None):

	if request.method == 'GET':
		form = LeagueForm()

		if sport_id is not None:
			sport = Sport.objects.get(id=sport_id)
			form = LeagueForm(initial={'sport': sport})

		return render(request, 'league.html', {'form': form})

	if request.method == 'POST':
		form = LeagueForm(request.POST)
		
		if form.is_valid():
			new_league = form.save()
			return redirect(reverse_lazy('settings:view_league', kwargs={'league_id': str(new_league.id)}))
			#return redirect(reverse_lazy('athletes:view', kwargs={'user_id': str(new_athlete.id)}))

		return render(request, 'league.html', {'form': form})


def edit_league(request, league_id):
	league = League.objects.get(id=league_id)

	if request.method == 'GET':
		form = LeagueForm(instance=league)
		return render(request, 'league.html', {'form': form, 'editing':True, 'league':league})

	if request.method == 'POST':
		form = LeagueForm(request.POST, instance=league)
		
		if form.is_valid():
			league = form.save()
			return redirect(reverse_lazy('settings:view_league', kwargs={'league_id': str(league.id)}))
			#return redirect(reverse_lazy('athletes:view', kwargs={'user_id': str(new_athlete.id)}))

		return render(request, 'league.html', {'form': form, 'editing':True, 'league':league})


def view_league(request, league_id):
	league = League.objects.get(id=league_id)
	return render(request, 'league_detail.html', {'league': league})


def delete_league(request, league_id):
	league = League.objects.get(id=league_id)
	league.delete()

	return redirect(reverse_lazy('settings:leagues_index'))








def clubs_index(request):
	clubes = Club.objects.all()
	return render(request, "clubs.html", {'clubes':clubes})


def create_club(request, league_id=None):

	if request.method == 'GET':

		form = ClubForm()
		if league_id is not None:
			league = League.objects.get(id=league_id)
			form = ClubForm(initial={'league': league})

		return render(request, 'club.html', {'form': form})

	if request.method == 'POST':
		form = ClubForm(request.POST)
		
		if form.is_valid():
			new_club = form.save()
			return redirect(reverse_lazy('settings:view_club', kwargs={'club_id': str(new_club.id)}))
			#return redirect(reverse_lazy('athletes:view', kwargs={'user_id': str(new_athlete.id)}))

		return render(request, 'club.html', {'form': form})


def edit_club(request, club_id):
	club = Club.objects.get(id=club_id)

	if request.method == 'GET':
		form = ClubForm(instance=club)
		return render(request, 'club.html', {'form': form, 'editing':True, 'club':club})

	if request.method == 'POST':
		form = ClubForm(request.POST, instance=club)
		
		if form.is_valid():
			club = form.save()
			return redirect(reverse_lazy('settings:view_club', kwargs={'club_id': str(club.id)}))
			#return redirect(reverse_lazy('athletes:view', kwargs={'user_id': str(new_athlete.id)}))

		return render(request, 'club.html', {'form': form, 'editing':True, 'club':club})


def view_club(request, club_id):
	club = Club.objects.get(id=club_id)
	return render(request, 'club_detail.html', {'club': club})


def delete_club(request, club_id):
	club = Club.objects.get(id=club_id)
	club.delete()

	return redirect(reverse_lazy('settings:clubs_index'))