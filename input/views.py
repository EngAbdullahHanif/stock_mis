from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views import generic
from django.views.generic import TemplateView
from django.views.generic import CreateView, ListView, UpdateView, DetailView
from django.urls import reverse_lazy
from django.utils import timezone
from datetime import datetime, timedelta
from django.db.models import Sum, F
from django.db.models.functions import ExtractWeekDay
from django.core.exceptions import ObjectDoesNotExist
from django.db import transaction, models
from django.shortcuts import get_object_or_404


from bootstrap_modal_forms.generic import (
    BSModalDeleteView,
    BSModalCreateView,
    BSModalUpdateView,
    BSModalReadView,
)


from .models import SuggestionForm, M3Form, M7Form, M10Form
from .forms import SuggestionForm_Form, M3Form_Form, M3FormDetail_Form



class SuggestionFormCreateView(SuccessMessageMixin, CreateView):
    model = SuggestionForm
    template_name = "input/suggestion_form_create.html"
    form_class = SuggestionForm_Form
    success_url = reverse_lazy('suggestion-form-create')
    success_message = 'موفقانه ثبت گردید'


class SuggestionFormListView(ListView):
    def get(self, *args, **kwargs):
        sugg_forms = SuggestionForm.objects.all()
        context = {
            'sugg_forms': sugg_forms
        }
        return render(self.request, 'input/suggestion_form_list.html', context)


class SuggestionFormUpdateView(SuccessMessageMixin, UpdateView):
    model = SuggestionForm
    template_name = 'input/suggestion_form_create.html'
    form_class = SuggestionForm_Form
    success_url = reverse_lazy('suggestion-forms-list')
    success_message = 'موفقانه اپدیت گردید'


class SuggestionFormDeleteView(SuccessMessageMixin, BSModalDeleteView):
    model = SuggestionForm
    template_name = 'input/modals/sugg_form_delete.html'
    success_url = reverse_lazy('suggestion-forms-list')
    success_message = 'موفقانه حذف گردید'


class SuggestionFormDetailView(DetailView):
    model = SuggestionForm
    template_name = 'input/sugg_form_detail.html'
    context_object_name = 'sugg_form'


class SuggestionForm1ListView(ListView):
    def get(self, *args, **kwargs):
        sugg_forms = SuggestionForm.objects.all().filter(dean_commandment="")
        context = {
            'sugg_forms': sugg_forms
        }
        return render(self.request, 'input/suggestion_form_list.html', context)

class SuggestionForm1UpdateView(SuccessMessageMixin, UpdateView):
    model = SuggestionForm
    template_name = 'input/suggestion_form_create.html'
    form_class = SuggestionForm_Form
    success_url = reverse_lazy('suggestion-forms-list')
    success_message = 'موفقانه اپدیت گردید'
    

class SuggestionForm2ListView(ListView):
    def get(self, *args, **kwargs):
        sugg_forms = SuggestionForm.objects.all().filter(addminstartion_commandment="")
        context = {
            'sugg_forms': sugg_forms
        }
        return render(self.request, 'input/suggestion_form_list.html', context)

class SuggestionForm2UpdateView(SuccessMessageMixin, UpdateView):
    model = SuggestionForm
    template_name = 'input/suggestion_form_create.html'
    form_class = SuggestionForm_Form
    success_url = reverse_lazy('suggestion-forms-list')
    success_message = 'موفقانه اپدیت گردید'


class M3FormCreateView(CreateView):
    model = M3Form
    template_name = 'input/m3forms/m3form_create.html'
    form_class = M3Form_Form
    success_url = reverse_lazy('suggestion-forms-list')
    success_message = 'فورم ایم-3 موفقانه برای پیشنهاد ثبت گردید'


class Suggesstion_M3FormDetail(DetailView):
    model = M3Form
    template_name = 'input/m3form.html'
    context_object_name = 'm3obj'

class Suggesstion_M7FormDetail(DetailView):
    model = M7Form
    template_name = 'input/m7form.html'
    context_object_name = 'm7obj'


class Suggesstion_M10FormDetail(DetailView):
    model = M10Form
    template_name = 'input/m10form.html'
    context_object_name = 'm10obj'



    # def get_context_data(self, **kwargs):
    #     context = super(M3FormCreateView, self).get_context_data(**kwargs)
    #     # clients = ModelChoiceField(queryset=Client.objects.all())
    #     if self.request.POST:
    #         context['items'] = M3FormDetail_Form(self.request.POST)
    #         # context['account'] = AccountFormSet(self.request.POST)
    #         # context['clients'] = clients
    #     else:
    #         context['items'] = M3FormDetail_Form()
    #         # context['account'] = AccountFormSet()
    #         # context['clients'] = Client.objects.all()
    #     return context

    # def form_valid(self, form):
    #     context = self.get_context_data()
    #     items = context['items']
    #     # account = context['account']
    #     with transaction.atomic():
    #         self.object = form.save()

    #         if items.is_valid():
    #             items.instance = self.object
    #             # account.instance = self.object
    #             # print(account.POST['client'])
    #             print(items)
    #             items.save()
    #             # account.save()
    #     return super(M3FormCreateView, self).form_valid(form)

    # def get_form(self, *args, **kwargs):
    #     form = super(M3FormCreateView, self).get_form(*args, **kwargs)
    #     form.fields['suggestion_form'].queryset = SuggestionForm.objects.all()
    #     #form.fields['delivery_date'].widget = forms.DateField(widget=forms.CharField(attrs={'type': 'date'}), label='تاریخ رسید ')
    #     return form

    # def post(self, *args, **kwargs):
    #     form = M3Form_Form(self.request.POST)
    #     sug_form = kwargs['pk']
    #     form_instance = M3Form.objects.get(id=sug_form)

    #     if form.is_valid():
    #         purchase_order_num = form.cleaned_data.get('porterage_expenses')
    #         issued_date = form.cleaned_data.get('issued_date')
    #         purchase_suggestion_num = form.cleaned_data.get('purchase_suggestion_num')
    #         # description = form.cleaned_data.get('description')
    #         # item = form.cleaned_data.get('item')
    #         # quantity = form.cleaned_data.get('quantity')
    #         # module = form.cleaned_data.get('module')
    #         # price = form.cleaned_data.get('price')

    #         m3form = M3Form(
    #             purchase_order_num = purchase_order_num,
    #             issued_date = issued_date,
    #             purchase_suggestion_num = purchase_suggestion_num,
    #             # description = description,
    #             # item = item,
    #             # quantity = quantity,
    #             # module = module,
    #             # price = price,
    #             suggestion_form=form_instance,
    #         )
    #         m3form.save()
    #         messages.success(self.request, 'فورم ایم-3 موفقانه برای پیشنهاد ثبت گردید')
    #         return redirect('suggestion-forms-list')

    #     messages.success(self.request, 'فورم ایم-3 موفقانه برای پیشنهاد ثبت نه گردید')
    #     return redirect('suggestion-forms-list')

    # def get(self, *args, **kwargs):
    #     form = kwargs['pk']
    #     try:
    #         form_instance = M3Form.objects.get(id=form)
    #     except M3Form.DoesNotExist:
    #         form_instance = None

    #     if M3Form.objects.filter(suggestion_form=form_instance).exists():
    #         messages.info(self.request, 'فورم ایم-3 از قبل ثبت گردیده است')
    #         return redirect('suggestion-forms-list')
    #     return super(M3FormCreateView, self).get(*args, **kwargs)


class M3FormListView(ListView):
    model = M3Form
    template_name = 'input/m3form_list.html'
    context_object_name = 'm3objs'


class M7FormListView(ListView):
    model = M7Form
    template_name = 'input/m7form_list.html'
    context_object_name = 'm7objs'


class M10FormListView(ListView):
    model = M10Form
    template_name = 'input/m10form_list.html'
    context_object_name = 'm10objs'


class M3FormDetail(DetailView):
    model = M3Form
    template_name = 'input/m3form.html'
    context_object_name = 'm3obj'

    # def get(self, *args, **kwargs):
    #     form = kwargs['pk']
    #     m3obj = M3Form.objects.get(id=form)
    #     m3obj_items = m3obj.m3formdetail_set.all()
    #     print('**************************************')
    #     print(m3obj_items)
    #     context = {
    #         'm3obj': m3obj,
    #         'm3obj_items': m3obj_items,
    #     }
    #     return render(self, 'input/m3form.html', context)

def m3form_detail(request, pk):
        form = pk
        m3obj = M3Form.objects.get(id=form)
        m3obj_items = m3obj.m3formdetail_set.all()
        total_amount = sum([m3obj_item.price for m3obj_item in m3obj_items])
        print('**************************************')
        print(total_amount)
        context = {
            'm3obj': m3obj,
            'm3obj_items': m3obj_items,
            'total_amount': total_amount,
        }
        return render(request, 'input/m3form.html', context)



class M7FormDetail(DetailView):
    model = M7Form
    template_name = 'input/m7form.html'
    context_object_name = 'm7obj'


def m7form_detail(request, pk):
        form = pk
        m7obj = M7Form.objects.get(id=form)
        m7obj_items = m7obj.m7formdetail_set.all()
        total_amount = sum([m7obj_item.amount for m7obj_item in m7obj_items])
        print('**************************************')
        print(total_amount)
        context = {
            'm7obj': m7obj,
            'm7obj_items': m7obj_items,
            'total_amount': total_amount,
        }
        return render(request, 'input/m7form.html', context)

class M10FormDetail(DetailView):
    model = M10Form
    template_name = 'input/m10form.html'
    context_object_name = 'm10obj'


# class DeliveryCreateView(SuccessMessageMixin, CreateView):
#     model = Delivery
#     template_name = "sales/delivery_create.html"
#     # fields = ['delivery_date', 'receipt_number', 'client', 'saller']
#     success_message = 'موفقانه ثبت کردید'
#     success_url = reverse_lazy('delivery-create')
#     form_class = DelivieyForm

#     def get_context_data(self, **kwargs):
#         context = super(DeliveryCreateView, self).get_context_data(**kwargs)
#         # clients = ModelChoiceField(queryset=Client.objects.all())
#         if self.request.POST:
#             context['items'] = ItemsFormSet(self.request.POST)
#             # context['account'] = AccountFormSet(self.request.POST)
#             # context['clients'] = clients
#         else:
#             context['items'] = ItemsFormSet()
#             # context['account'] = AccountFormSet()
#             # context['clients'] = Client.objects.all()
#         return context

#     def form_valid(self, form):
#         context = self.get_context_data()
#         items = context['items']
#         # account = context['account']
#         with transaction.atomic():
#             self.object = form.save()

#             if items.is_valid():
#                 items.instance = self.object
#                 # account.instance = self.object
#                 # print(account.POST['client'])
#                 print(items)
#                 items.save()
#                 # account.save()
#         return super(DeliveryCreateView, self).form_valid(form)

#     def get_form(self, *args, **kwargs):
#         form = super(DeliveryCreateView, self).get_form(*args, **kwargs)
#         form.fields['client'].queryset = Client.objects.all()
#         #form.fields['delivery_date'].widget = forms.DateField(widget=forms.CharField(attrs={'type': 'date'}), label='تاریخ رسید ')
#         return form
