from django.db import models
from django.conf import settings

# Create your models here.

"""
TO use when image is being used in interview class.
def upload_location(Post, filename):
    return "%s/%s/%s" %(Post.app_name,Post.user, filename)


"""


class contact_details(models.Model):
	CONTACT_LIST = (
		('email', 'Email'),
		('facebook', 'Facebook'),
		('twitter', 'Twitter'),
		('instagram', 'Instagram'),
		('reddit', 'Reddit'),
		)
	
	user					=			models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE)
	
	contact_form			=			models.CharField(max_length=20, choices=CONTACT_LIST, default=CONTACT_LIST[0][0])
	contact					=			models.CharField(max_length=100, blank=False, null=False, help_text="Guest contact name.")
	
	timestamp				=			models.DateTimeField(auto_now=False, auto_now_add=True)
	updated					=			models.DateTimeField(auto_now=True, auto_now_add=False)
  
	def __str__(self):
		return(self.contact + str(' | ') + self.contact_form)

	class Meta:
		ordering	 		=			["-timestamp", "-updated"]
		verbose_name 		= 			"Contact Detail"
		verbose_name_plural = 			"Contact Details"



class queue(models.Model):	
	user					=			models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE)
	
	guest 					=			models.CharField(max_length=200, blank=False, null=False)

	confirmation			=			models.BooleanField(default=False)
	guest_contact			=			models.ManyToManyField('contact_details', related_name='guest_queue', blank=True)
	
	timestamp				=			models.DateTimeField(auto_now=False, auto_now_add=True)
	updated					=			models.DateTimeField(auto_now=True, auto_now_add=False)

	def __str__(self):
		return(self.guest + str(' | ') + self.confirmation)

	class Meta:
		ordering	 		=			["-timestamp", "-updated"]
		verbose_name 		= 			"Queue"
		verbose_name_plural = 			"Queues"


class interview(models.Model):
	user					=			models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE)
	"""
		Me, the article writer.

	"""
	
	title					=			models.CharField(max_length=280, blank=False, null=False)
	"""
		Title of the blog.
	"""
	company_name			=			models.CharField(max_length=100, blank=True, null=True)
	"""
		The Name of the company
	"""
	location				=			models.CharField(max_length=50, blank=False, null=False)
	"""
		City, Country. if null leave out.
	"""
	revenue					=			models.CharField(max_length=20, blank=False, null=False)
	"""
		This is a combined revenue. total.
		TODO: Add a foreign key field for adding all the revenue sources.

		The revenue field is Charfield so that we can have flexibility in terms of the unit.
		it could be $2000 per month, or $3000-$6000 per month, also the currency could be any currency.
	"""
	started					=			models.DateField(blank=False)
	work_description		=			models.TextField(max_length=280, blank=False, null=False)
	# Use this as the Social media Text.

	"""
	Social media: Twitter Card.

	Title 					= (67) Python Scripting APIs in Cisco DNA Center Let You Improve Effective
	description 			= (138) See how you can use the DNA Center APIs in a Python script to get information on all of the network devices the DNCA controller knows abou...

	"""
	
	# The actual blog, piece
	detail					=			models.TextField(max_length=23000, blank=True, null=True, default='')

	"""
		TODO:
		1. Add a social media links, like the way i saw in the blog of Nicole Harris.
		# social_media_foreign	=			models.CharField(max_length=10, blank=False, null=False)

		2. Social Media Image, to be shared on for twitter and facebook.
	    image = models.ImageField(
	        upload_to=upload_location,
	        null = True,
	        blank = True,
	        height_field = "height_field",
	        width_field = "width_field",
	    )
	    height_field = models.IntegerField(default=0)
	    width_field = models.IntegerField(default=0)

	"""


	source_name				=			models.CharField(max_length=50, blank=True, null=True, default="")
	source_description		=			models.TextField(max_length=280, blank=True, null=True, default="")
	# To Avoid spam content
	public_display			=			models.BooleanField(default=False)
	website					=			models.URLField(max_length=1000, blank=False, null=False, help_text="Your Landing page URL.")
	
	timestamp				=			models.DateTimeField(auto_now=False, auto_now_add=True)
	updated					=			models.DateTimeField(auto_now=True, auto_now_add=False)

	def __str__(self):
		return(self.title)
	class Meta:
		ordering	 		=			["-timestamp", "-updated"]
		verbose_name 		= 			"Interview"
		verbose_name_plural = 			"Interviews"

