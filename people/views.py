from django.shortcuts import render, get_object_or_404, redirect, HttpResponseRedirect, render_to_response
from django.http import HttpResponse, Http404
from django.urls import reverse

from .models import interview, contact_details
from .forms import InterviewRequestForm
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

	if this_interview.public_display:
		pass
	else:
		if not request.user.is_superuser:
			raise Http404
		else:
			pass


	context = {
		"interview" : this_interview,
		'show_last_div' : True,
	}
	return render(request, 'people/interview_detail.html', context)

def why_interview(request):
	context = {
		'show_last_div' : False,
	}
	return render(request, 'people/why_interview.html', context)

def interview_request(request):
	if request.method == 'POST':
		form = InterviewRequestForm(request.POST or None)
		if form.is_valid():
			# product_name = form.cleaned_data.get("product_name")
			instance = form.save(commit=False)
			instance.save()
			return HttpResponseRedirect(reverse('people:thankyou_page'))

	else:
		form = InterviewRequestForm()

	context = {
		'show_last_div' : False,
		'form' : form,
		"tab_text": "Confirm my Interview",
		"top_text": "Lets Book your Interview with Ali!",
		"form_text": "Please chose a communication channel, and provide us with your username. Or you can chose to give your email!",
	}
	return render(request, 'general_form.html', context)

def thankyou_page(request):
	context = {
		'show_last_div' : False,
	}
	return render_to_response('people/thankyou_page.html', context)