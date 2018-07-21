from django import forms
from django.core.validators import validate_email

from .models import contact_details

# Form for accepting new interviews
class InterviewRequestForm(forms.ModelForm):
	class Meta:
		model = contact_details
		fields = [
		'contact_form',
		'contact', 
		]


	def clean_contact(self):
		this_contact = self.cleaned_data.get('contact')
		this_contact_form = self.cleaned_data.get('contact_form')

		if this_contact_form == 'email':
			try:
				validate_email(this_contact)
			except forms.ValidationError:
				raise forms.ValidationError("Please enter a Valid Email address")

		existing_contact = contact_details.objects.filter(contact=this_contact, contact_form=this_contact_form)

		if existing_contact:
			raise forms.ValidationError("You already submitted a request with these credentials")
		else:
			return this_contact

	def __init__(self, *args , **kwargs):
		super(InterviewRequestForm, self).__init__(*args, **kwargs)
		self.fields["contact_form"].help_text = "Select a social media to get in contact with you, example: Twitter, or an email"
		self.fields["contact"].help_text = "Enter your User ID or e-mail"
		self.fields["contact"].label = "User ID"
		self.fields["contact_form"].label = "Platform"
