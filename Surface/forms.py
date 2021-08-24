from django import forms
from Surface.models import WorkDetail

class WorkDetailForm(forms.ModelForm):
	class Meta:
		model = WorkDetail
		fields = "__all__"