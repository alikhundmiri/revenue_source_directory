from django.shortcuts import render, get_object_or_404, redirect
from .models import interview
# Create your views here.


# def platform_list(request):
# 	interviews = interview.objects.all()
# 	count_ads = ads.objects.count()
# 	adverts = fetch_adverts(1) # This number is the amount of ads
# 	all_platforms = platform.objects.filter(all_sources__public_display=True, public_display=True).distinct()
# 	context = {
# 	'interviews' : interviews,
# 	"all_platforms" : all_platforms,
# 	"adverts" :adverts,
# 	"production" : settings.PRODUCTION,
# 	}
# 	return render(request, 'platform_list.html', context)

def interview_detail(request, id_=None):
	this_interview = get_object_or_404(interview, id=id_)
	context = {
		"interview" : this_interview,
	}
	return render(request, 'people/interview_detail.html', context)