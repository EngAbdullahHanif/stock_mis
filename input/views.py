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

from bootstrap_modal_forms.generic import (
    BSModalDeleteView,
    BSModalCreateView,
    BSModalUpdateView,
    BSModalReadView,
)


from .models import SuggestionForm
from .forms import SuggestionForm_Form



class SuggestionFormCreateView(SuccessMessageMixin, CreateView):
    model = SuggestionForm
    template_name = "input/suggestion_form_create.html"
    form_class = SuggestionForm_Form
    success_url = reverse_lazy('suggestion-form-create')
    success_message = 'موفقانه ثبت کردید'


class SuggestionFormListView(ListView):
    def get(self, *args, **kwargs):
        sugg_forms = SuggestionForm.objects.all()
        context = {
            'sugg_forms': sugg_forms
        }
        return render(self.request, 'input/suggestion_form_list.html', context)


class SuggestionFormUpdateView(SuccessMessageMixin, UpdateView):
    model = SuggestionForm
    template_name = 'input/suggestion_form_update.html'
    form_class = SuggestionForm_Form
    success_url = reverse_lazy('suggestion-form-create')
    success_message = 'موفقانه اپدیت کردید'


class SuggestionFormDeleteView(SuccessMessageMixin, BSModalDeleteView):
    model = SuggestionForm
    template_name = 'input/modals/suggestion_form_delete.html'
    success_url = reverse_lazy('suggestion-form-list')
    success_message = 'موفقانه حذف کردید'


class SuggestionFormDetailView(DetailView):
    model = SuggestionForm
    template_name = 'input/suggestion_form_detail.html'
    context_object_name = 'sugg_form'
