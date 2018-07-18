from random import randint
from django.conf import settings
from django.shortcuts import render, get_object_or_404, redirect


from .models import Type_of_Platform, platform, sources

from advertisment.models import ads
from people.models import interview

from advertisment.views import fetch_adverts

def index(request):
	context = {}
	return render(request, 'temp_file.html', context)


'''
NOTE: This view will load only the list of platforms.

When clicked it should takee the use to the said platform, before marking the page as clicked
and incrememting the counter

'''


def platform_list(request):
	interviews = interview.objects.filter(public_display=True)
	count_ads = ads.objects.count()
	adverts = fetch_adverts(1) # This number is the amount of ads
	all_platforms = platform.objects.filter(all_sources__public_display=True, public_display=True).distinct()
	context = {
	'interviews' : interviews,
	"all_platforms" : all_platforms,
	"adverts" :adverts,
	"production" : settings.PRODUCTION,
	}
	return render(request, 'platform_list.html', context)
