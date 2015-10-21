
from django.conf.urls import include, url
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin

from .views import ContactFormView, ContactFormTag

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^form-tag$', ContactFormTag.as_view(), name='form-tag'),
    url(r'^$', ContactFormView.as_view(), name='contact'),
]
