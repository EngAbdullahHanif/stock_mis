from django.forms import ModelForm
from django import forms
from bootstrap_modal_forms.forms import BSModalModelForm

from .models import SuggestionForm

class SuggestionForm_Form(ModelForm):
    class Meta():
        model = SuggestionForm
        fields = [
            'number',
            'issued_date',
            'deanship',
            'department',
            'topic',
            'description',
            'dean',
            'dean_commandment',
            'addminstartion_commandment',
            'advice_commitee',
            'addminstration_final'
        ]
