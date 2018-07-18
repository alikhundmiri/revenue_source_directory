from django.contrib import admin

from .models import interview

class InterviewAdmin(admin.ModelAdmin):
	list_display = ['company_name', 'title', 'location', 'revenue', 'started', 'work_description', 'public_display', 'website', ]
	list_filter = ['title', 'company_name', 'location', 'revenue', 'started', 'work_description', 'public_display', 'website', ]
	search_fields = ['title', 'company_name', 'location', 'revenue', 'started', 'work_description', 'public_display', 'website', 'detail' ]
	list_editable = ['title']
	class Meta:
		model = interview

admin.site.register(interview, InterviewAdmin)
