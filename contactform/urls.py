
from django.conf.urls import include, url
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin

from .views import ContactFormView, ContactFormTagView

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^form-tag$', ContactFormTagView.as_view(), name='form-tag'),
    url(r'^contact$', ContactFormView.as_view(), name='contact'),
]
