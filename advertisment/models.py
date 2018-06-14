from django.conf import settings
from django.db import models
from django.db.models.signals import pre_save, post_save

from datetime import datetime, timedelta

def advertisment_image_location(platform, filename):
	return "%s/%s/%s/%s" %("advertisment", platform.user, platform.id, filename)

class ads(models.Model):
	AD_STATUS = (
		("Unpaid", 'unpaid'),
		("Paid", 'paid'),
		('Displaying', 'displaying'),
		('Completed', 'completed'),
		)
	AD_LIFE = (
		(1, "1 Day"),
		(7, "7 Days"),
		(28, "28 Days"),
		)

	# who is uploading this product
	user					=			models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE)
	image 					= 			models.ImageField(
											upload_to=advertisment_image_location,
											null = True,
											blank = True,
											height_field = "height_field",
											width_field = "width_field",
										)
	height_field			=			models.IntegerField(default=0)
	width_field				=			models.IntegerField(default=0)

	# the product name
	client_name				=			models.CharField(max_length=50, blank=False, null=False, default="")
	client_description		=			models.TextField(max_length=280, blank=True, null=True, default="")

	# To Avoid spam content
	public_display			=			models.BooleanField(default=False)
	# If the product is uploaded by the maker, this needs to be done manually.
	# product_verified 		=			models.BooleanField(default=False)
	website					=			models.URLField(max_length=1000, blank=False, null=False, help_text="Your Landing page URL.")
	click_count				=			models.IntegerField(default=0)

	# alias of advert_end
	advert_time 			=			models.DateTimeField(editable=True, default=datetime.now)

	advert_status			=			models.CharField(max_length=20, choices=AD_STATUS, default=AD_STATUS[0][0])

	advert_view 			=			models.IntegerField(default=0)

	advert_lifespan			=			models.IntegerField(choices=AD_LIFE, default=AD_LIFE[0][0], help_text="Number of days you want the advert to be live")


	timestamp				=			models.DateTimeField(auto_now=False, auto_now_add=True)
	updated					=			models.DateTimeField(auto_now=True, auto_now_add=False)

	def __str__(self):
		return(self.client_name)



def post_save_advert_time(sender, instance, *args, **kwargs):
	# instance.slug = change_date(instance)
	# if the advert_status is paid move forward to change end date, else pass
	# if public_display, 

	# check if advert_status is 'Paid'
	if instance.advert_status == instance.AD_STATUS[1][0]:
		# Change the end date
		change_date(instance)
		# change the ad_status to Displaying
		change_ad_status(instance)
		instance.save()


def change_date(instance):
	'''
	DONE: fetch the advert_lifespan
	DONE: get updated date
	
	DONE: increment the current date with advert_lifespan
	DONE: save that date to advert_time
	'''
	# print("instance.updated : " + str(instance.updated) + str(type(instance.updated)))

	# fetch the advert_lifespan
	point_zero = instance.updated

	# get updated date
	additional_days = instance.advert_lifespan
	
	#  add new date to the updated date.
	new_date = point_zero+timedelta(days=additional_days)

	# print("point_zero : " + str(point_zero) + str(type(point_zero)))
	# print("additional_days : " + str(additional_days) + str(type(additional_days)))
	# print("new_date : " + str(new_date) + str(type(new_date)))
	
	# apply is to the actual field
	instance.advert_time = new_date

def change_ad_status(instance):
	instance.advert_status = instance.AD_STATUS[2][0]
	# print("changed the status to Displaying")


post_save.connect(post_save_advert_time, sender=ads)
