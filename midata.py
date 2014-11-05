import requests
import jsonapi

# constants
user_path          = '/groups/1/people/{}'
group_path         = '/groups/{}'
group_members_path = '/groups/{}/people'
valid_group_roles  = {'Abteilungsleiter'}


class Person(object):
    def __init__(self, json):
        pass

class Group(object):
    def __init__(self, json):
        pass

class MiData(object):
    _json_cache = None

    def __init__(self):
        self._json_cache = jsonapi.Cache()

    def fetch_person(auth_info, person_id):
        pass

    def fetch_group(auth_info, group_id):
        pass

    def fetch_members(auth_info, group_id):
        pass

    def _fetch_content(auth_info, url):
        r = requests.get(server + user_path.format(auth_info.user_id),
                         headers=auth_info.http_headers())

        if r.status_code != 200:
            raise Exception("Error!")

        json_cache.update(r.json())
    
    
