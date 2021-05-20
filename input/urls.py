from django.urls import path


from .views import(
    SuggestionFormCreateView, SuggestionFormListView, SuggestionFormDetailView, SuggestionFormUpdateView, SuggestionFormDeleteView,
    SuggestionForm1ListView, SuggestionForm1UpdateView, SuggestionForm2ListView, SuggestionForm2UpdateView,
    M3FormCreateView, M3FormDetail, M7FormDetail, M10FormDetail, M3FormListView, M7FormListView, M10FormListView, Suggesstion_M3FormDetail, Suggesstion_M7FormDetail, Suggesstion_M10FormDetail,

    m3form_detail, m7form_detail
) 

urlpatterns = [
    path('', SuggestionFormListView.as_view(), name='suggestion-forms-list'),
    path('/create', SuggestionFormCreateView.as_view(), name='suggestion-form-create'),
    path('<pk>', SuggestionFormDetailView.as_view(), name='suggestion-form-detail'),
    path('form/<int:pk>/update', SuggestionFormUpdateView.as_view(), name='suggestion-form-update'),
    path('form/<int:pk>/delete', SuggestionFormDeleteView.as_view(), name='suggestion-form-delete'),

    path('/form1/', SuggestionForm1ListView.as_view(), name='suggestion-form1s-list'),
    path('/form1/<int:pk>/update', SuggestionForm1UpdateView.as_view(), name='suggestion-form1s-update'),
    path('/form2/', SuggestionForm2ListView.as_view(), name='suggestion-form2s-list'),
    path('/form2/<int:pk>/update', SuggestionForm2UpdateView.as_view(), name='suggestion-form2s-update'),

    path('/form/m3form', M3FormCreateView.as_view(), name="m3form-create"),

    path('/m3form/<int:pk>', Suggesstion_M3FormDetail.as_view(), name='sug-m3form'),
    path('/m7form/<int:pk>', Suggesstion_M7FormDetail.as_view(), name='sug-m7form'),
    path('/m10form/<int:pk>', Suggesstion_M10FormDetail.as_view(), name='sug-m10form'),

    path('/m3form', M3FormListView.as_view(), name='m3forms-list'),
    path('/m7form', M7FormListView.as_view(), name='m7forms-list'),
    path('/m10form', M10FormListView.as_view(), name='m10forms-list'),

    path('/m3form-detail/<int:pk>', m3form_detail, name='m3form'),
    path('/m7form-detail/<int:pk>', m7form_detail, name='m7form'),
    path('/m10form-detail/<int:pk>', M10FormDetail.as_view(), name='m10form'),



]
    