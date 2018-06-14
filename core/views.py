from django.shortcuts import render
from random import randint
from django.conf import settings


from .models import Type_of_Platform, platform, sources
from advertisment.models import ads
from advertisment.views import fetch_adverts

def index(request):
	context = {}
	return render(request, 'temp_file.html', context)

def platform_list(request):
	count_ads = ads.objects.count()
	adverts = fetch_adverts(1) # This number is the amount of ads
	all_platforms = platform.objects.filter(all_sources__public_display=True, public_display=True).distinct()
	context = {
	"all_platforms" : all_platforms,
	"adverts" :adverts,
	"production" : settings.PRODUCTION,
	}
	return render(request, 'platform_list.html', context)