from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'travelplanner.views.index'),
    url(r'^travel/', include('travelplanner.urls'))
)
