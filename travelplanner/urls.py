from django.conf.urls import patterns, include, url

urlpatterns = patterns('travelplanner.views',
        (r'^$', 'index'),
        )
