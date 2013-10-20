from django.conf.urls import patterns, include, url

urlpatterns = patterns('travelplanner.views',
        (r'^(?P<travel_uri>\w+)$', 'travel'),

        # post requests

        (r'^api/set-email$', 'set_my_email'),
        (r'^api/invite-friends$', 'invite_friends'),

        (r'^api/travel-name-edit$', 'travel_name_edit'),
        (r'^api/map/add-place$', 'map_add_place'),
        (r'^api/map/remove-place$', 'map_remove_place'),
        (r'^api/place/add-activity$', 'activity_add'),
        (r'^api/place/edit-activity$', 'activity_edit'),
        (r'^api/place/remove-activity$', 'activity_remove'),

        (r'^api/map/get-places$', 'map_get_places'),
        (r'^api/place/get-activities$', 'place_get_activities'),
        )
