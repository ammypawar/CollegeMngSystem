from django import forms
from .models import Institute

class InstituteForm(forms.ModelForm):
	class Meta:
		model = Institute
		fields = ["reg_no","uni_soc_name","institute_name","mobile","email","address","url"]

	