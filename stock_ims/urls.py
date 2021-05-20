from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from .views import HomeView


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('advanced_filters', include('advanced_filters.urls')),
    path('', HomeView.as_view(), name='home'),
    path('form', include('input.urls')),
]




if settings.DEBUG == True:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    # urlpatterns += static(settings.MEDIA_URL,
    #                       document_root=settings.MEDIA_ROOT)


admin.site.site_header = "سیستم مدیریت گدامداری"
admin.site.site_title = "سیستم مدیریت گدامداری"
admin.site.index_title = "سیستم مدیریت گدامداری"