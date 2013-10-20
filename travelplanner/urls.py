from django.conf.urls import patterns, include, url

urlpatterns = patterns('travelplanner.views',
        (r'^(?P<travel_uri>\w+)$', 'travel'),
        (r'^api/travel-name-edit$', 'travel_name_edit'),
        (r'^api/map/add-place$', 'map_add_place'),
        (r'^api/map/remove-place$', 'map_remove_place'),
        (r'^api/activity/add$', 'activity_add'),
        (r'^api/activity/edit$', 'activity_edit'),
        (r'^api/activity/remove$', 'activity_remove'),
        )
