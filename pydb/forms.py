from django import forms
from .models import Dancer


class DancerForm(forms.ModelForm):
    model = forms.Form
    fields = ['dancer_name', 'crew_id', 'style_id']

    class Meta:
        model = Dancer
        fields = ['dancer_name', 'crew_id', 'style_id']
