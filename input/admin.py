# from advanced_filters.admin import AdminAdvancedFiltersMixin

from django.contrib import admin
from django.contrib.admin import AdminSite
from rangefilter.filter import DateRangeFilter

from .models import SuggestionForm, M3Form, M3FormDetail, M7FormDetail, M11FormDetail, M10Form, M7Form, M11Form



class M3FormDetailInline(admin.StackedInline):
    model = M3FormDetail


class M3FormAdmin(admin.ModelAdmin):
    inlines = [
        M3FormDetailInline,
    ]
    list_display = ['suggestion_form', 'purchase_order_num', 'issued_date', 'purchase_suggestion_num']
    list_filter = ('suggestion_form', 'purchase_order_num', ('issued_date', DateRangeFilter), 'issued_date', 'purchase_suggestion_num')
    # list_filter = ['suggestion_form', 'purchase_order_num', 'issued_date', 'purchase_suggestion_num']



class M7FormDetailInline(admin.StackedInline):
    model = M7FormDetail


class M7FormAdmin(admin.ModelAdmin):
    inlines = [
        M7FormDetailInline,
    ]

    list_display = ['suggestion_form', 'report_num', 'issued_date']
    list_filter = ['suggestion_form', 'report_num', ('issued_date', DateRangeFilter), 'issued_date']



class M11FormDetailInline(admin.StackedInline):
    model = M11FormDetail


class M11FormAdmin(admin.ModelAdmin):
    inlines = [
        M11FormDetailInline,
    ]

    list_display = ['document_num', 'issued_date']
    list_filter = ['document_num', ('issued_date', DateRangeFilter), 'issued_date']


class SuggestionFormAdmin(admin.ModelAdmin):

    list_display = ['number', 'issued_date']
    list_filter = ['number', ('issued_date', DateRangeFilter), 'issued_date']


class M10FormAdmin(admin.ModelAdmin):

    list_display = ['suggestion_num', 'applicator', 'amount', 'issue_date']
    list_filter = ['suggestion_num', 'applicator', 'amount', ('issue_date', DateRangeFilter), 'issue_date']




admin.site.register(M11Form, M11FormAdmin)
admin.site.register(M10Form, M10FormAdmin)
admin.site.register(M7Form, M7FormAdmin)
admin.site.register(M3Form, M3FormAdmin)
admin.site.register(SuggestionForm, SuggestionFormAdmin)

