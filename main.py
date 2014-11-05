#!/usr/bin/env python3

import requests
import midata
from midata import authentication as auth

# input data
server   = "http://db.scout.ch"
email    = "user@pbs.ch"
password = "password"
group_id = 15

# log in
auth_info = auth.sign_in(server, email, password)
if not auth_info:
    pass

user = midata.get_person(auth_info, auth_info.user_id)

# figure out interesting groups
valid_group_roles  = {'Abteilungsleiter'}
group_lookup = {group['id']:group for group in user.groups}

roles = (role for role in user.roles
              if role['role_type'] in valid_group_roles)

groups = [group_lookup[role['links']['group']] for role in roles]

# SELECT ONE
group_id = '15'

def group_hierarchy(group_id):
    group = midata.get_group(auth_info, group_id)

    children = {child_id: group_hierarchy(child_id)
                          for child_id in group.children}

    return children

hierarchy = {group_id: group_hierarchy(group_id)}

def flatten(d):
    for (k,v) in d.items():
        yield(k)
        yield from flatten(v)

# grab all people and roles
group_members = {group_id: midata.get_members(auth_info, group_id)
                 for group_id in flatten(hierarchy)}

for group_id, members in group_members.items():
    print(group_id)
    print("=======")
    for member in members:
        print(member)
    print()

