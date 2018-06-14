from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from django.utils import timezone
import random

from .models import ads
# Create your views here.

def advert_redirect(request, id=None):
	# fetch the single ad object, or 404
	ad = get_object_or_404(ads, id=id)

	# the link from website item
	newlink = ad.website
	# increment the click count
	ad.click_count += 1

	# now check for if the time of advertisment is over.
	if timezone.now() > ad.advert_time:
		# if the number of clicks are equal to requested clicks, turn off the advert status
		ad_contract_completion(ad)
	else:
		pass
	# save the advert. 
	ad.save()
	# return to the link of this advert!
	return HttpResponseRedirect(newlink)



def ad_contract_completion(ad):
	ad.advert_time = adverts.AD_STATUS[3][0]
	pass

def fetch_adverts(number_of_ads):

	# ads.objects.filter(public_display=True)[randint(0, count_ads - 1)]

	LOAD_ADS = number_of_ads
	num_list = []
	# fetch ads
	fetch_ = ads.objects.filter(public_display=True ,advert_status=ads.AD_STATUS[2][0])
	# fetch the total number of ads available
	limit_ = fetch_.count()
	if limit_ == 0:
		# print("number of ads available: 0")
		# if there are no ads, return None
		return None
	elif limit_ <= LOAD_ADS:
		# print("number of ads available: " + str(limit_))
		# if the number of ads in database is less than requested number, then give all avaialble ads
		rand_ad = fetch_[:limit_]
	else:
		# print("number of ads available: " + str(limit_))
		# generate 3 number from the limited range
		num_list = random.sample(range(0, limit_), LOAD_ADS)
		# fetch those ads
		rand_ad = [fetch_[num] for num in num_list]
		# print(rand_ad)

	# print(rand_ad)
	# mark those ads with viewed!
	mark_viewed(rand_ad)
	return rand_ad

def mark_viewed(rand_ad):
	for ad in rand_ad:
		# increment the advert_view field
		ad.advert_view += 1
		ad.save()
		# print(ad.advert_view)
	pass
