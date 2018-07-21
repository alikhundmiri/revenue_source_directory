from django.contrib import admin

from .models import interview, contact_details, queue

class InterviewAdmin(admin.ModelAdmin):
	list_display = ['title','company_name', 'location','public_display', 'website', ]
	list_filter = ['title', 'company_name', 'location', 'revenue', 'started', 'work_description', 'public_display', 'website', ]
	search_fields = ['title', 'company_name', 'location', 'revenue', 'started', 'work_description', 'public_display', 'website', 'detail' ]
	list_editable = []
	class Meta:
		model = interview

class ContactsAdmin(admin.ModelAdmin):
	list_display = ['user', 'contact', 'contact_form']
	list_filter = ['user', 'contact', 'contact_form']
	search_fields = ['user', 'contact', 'contact_form']
	list_editable = ['contact', 'contact_form']

	class Meta:
		model = contact_details

class QueueAdmin(admin.ModelAdmin):
	list_display = ['user', 'guest', 'confirmation',]
	list_filter = ['user', 'guest', 'confirmation', 'guest_contact']
	search_fields = ['user', 'guest', 'confirmation', 'guest_contact']
	list_editable = ['confirmation',]
	filter_horizontal = ['guest_contact']
	
	class Meta:
		model = queue


admin.site.register(interview, InterviewAdmin)
admin.site.register(contact_details, ContactsAdmin)
admin.site.register(queue, QueueAdmin)