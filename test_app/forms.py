from django import forms
from .models import Autohaus

class AutohausForm(forms.ModelForm):
    class Meta:
        model = Autohaus
        fields = ['brand_auto', 'model_auto', 'engine_fuel', 'engine_volume', 'description', 'link', 'auto_img', '']