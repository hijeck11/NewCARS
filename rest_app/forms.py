from django import forms
from .models import AutohausREST

class AutohausRESTForm(forms.ModelForm):
    class Meta:
        model = AutohausREST
        fields = '__all__'