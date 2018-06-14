from django.contrib import admin
from .models import ads


class AdsAdmin(admin.ModelAdmin):
	list_display = ["client_name", "user",'advert_time',"updated", 'click_count', 'advert_view','advert_status', "public_display",]
	list_filter = ["client_name","client_description", "timestamp", "updated", 'click_count', 'advert_time','advert_status', 'advert_view']
	search_fields = ["user", "client_name", "client_description", "public_display", "updated", 'click_count', 'advert_time','advert_status', 'advert_view']
	list_editable = ['public_display', 'advert_status']

	class Meta:
		model = ads

admin.site.register(ads, AdsAdmin)



