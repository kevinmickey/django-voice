from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView

admin.autodiscover()

urlpatterns = patterns(
    '',

    url(r'^$',
        view=TemplateView.as_view(template_name='home.html'),
        name='home'),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^comments/', include('django_comments.urls')),
    url(r'^feedback/', include('djangovoice.urls')),
    url(r'^auth/', include('django.contrib.auth.urls')),
    (r'^i18n/', include('django.conf.urls.i18n')),
)
