from django import forms
from bootstrap_modal_forms.forms import BSModalModelForm
from django.forms import ModelForm, inlineformset_factory

from .models import SuggestionForm, M3Form, M3FormDetail


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


class M3Form_Form(ModelForm):
    class Meta():
        model = M3Form
        fields = [
            'suggestion_form',
            'purchase_order_num',
            'issued_date',
            'purchase_suggestion_num',
        ]



class M3FormDetail_Form(ModelForm):
    # price =(error_messages={'invalid':"you custom error message"})
    class Meta():
        model = M3FormDetail
        fields = [
            'description',
            'item',
            'quantity',
            'module',
            'price',
        ]

        # error_messages = {
        #     'packing_type': {'required':'نوعیت بسته بندی الزامی میباشد.'},
        #     'gram_type': {'required':'نوعیت کرام الزامی میباشد.'},
        #     'quantity': {'required':'  مقدار الزامی میباشد.'},
        #     'price': {
        #         'required': 'قیمت الزامی میباشد.',
        #         'min_value': 'قیمت باید صفر یا از صفر بزرکتر باشد'}
        # }

ItemsFormSet = inlineformset_factory(M3Form, M3FormDetail, can_delete=False , form=M3FormDetail_Form,  extra=1)
ItemsUpdateFormSet = inlineformset_factory(M3Form, M3FormDetail, can_delete=False , form=M3FormDetail_Form,  extra=0)