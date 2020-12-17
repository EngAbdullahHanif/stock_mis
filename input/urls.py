from django.urls import path


from .views import SuggestionFormCreateView

urlpatterns = [
    path('', SuggestionFormCreateView.as_view(), name='suggestion-form-create')
]
