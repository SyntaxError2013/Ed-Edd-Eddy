from google.appengine.api import users
from django.shortcuts import redirect

import string
import random

def travel_uri_generator(size=11, chars=string.ascii_uppercase + string.digits): 
    return ''.join(random.choice(chars) for x in range(size))

def is_loggedin(request):
    user = users.get_current_user()
    if user is None:
        login_url = users.create_login_url(request.path)
        return login_url
    else:
        return None
