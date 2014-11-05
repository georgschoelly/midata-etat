#!/usr/bin/env python3

import requests
import authentication as auth
import jsonapi

# input data
server   = "http://db.scout.ch"
email    = "user@pbs.ch"
password = "password"
group_id = 15

# setup jsonapi cache
json_cache = jsonapi.Cache()

# log in
auth_info = auth.sign_in(server, email, password)
if not auth_info:
    pass

# get groups of user
groups = []
r = requests.get(server + user_path.format(auth_info.user_id),
                 headers=auth_info.http_headers())

if r.status_code != 200:
    raise Exception("Error!")

json_cache.update(r.json())

role_ids = json_cache.get('people', auth_info.user_id)['links']['roles']

top_groups = []
for role_id in role_ids:
    role = json_cache.get('roles', role_id)

    if role['role_type'] not in valid_group_roles:
        continue

    top_groups.append(json_cache.get('groups', role['links']['group']))

# SELECT ONE
group_id = '15'

def group_hierarchy(group_id):
    r = requests.get(server + group_path.format(group_id),
                     headers=auth_info.http_headers())

    if r.status_code != 200:
        raise Exception("Error!")

    json_cache.update(r.json())
    group = json_cache.get('groups', group_id)

    children = {child_id: group_hierarchy(child_id)
                          for child_id in group['links'].get('children', [])}

    return children

hierarchy = {group_id: group_hierarchy(group_id)}

def group_ids(d):
    for (k,v) in d.items():
        yield(k)
        yield from group_ids(v)

# grab all people and roles
for group_id in group_ids(hierarchy):
    r = requests.get(server + group_members_path.format(group_id),
                     headers=auth_info.http_headers())
    json_cache.update(r.json())

# assign members to each group
groups = {k: [] for k in groups_ids(hierarchy)}

for 

