import itertools
from copy import copy

_special_top_level_keys = {'linked', 'links', 'meta', 'data'}

class Cache(object):

    def __init__(self):
        self._object_cache = {}

    def get(self, type, key):
        return self._object_cache.get((type, key))

    def set(self, type, key, value):
        self._object_cache[(type, key)] = value

    def update(self, data_tree, top_type='data'):
        object_lists = []

        # the 'main' data can be either under the 'data' key or its type
        if top_type == 'data' and 'data' not in data_tree:
            names = set(data_tree.keys()) - _special_top_level_keys
            if len(names) != 1:
                raise Exception("Unable to figure out top-level data type.")

            top_type = names.pop()
            
        object_lists.append((top_type, data_tree[top_type]))

        # get linked items
        if 'linked' in data_tree:
            for (k,v) in data_tree['linked'].items():
                object_lists.append((k, v))

        # add items to cache
        for type, objs in object_lists:
            for obj in objs:
                if not self.get(type, obj['id']):
                    self.set(type, obj['id'], copy(obj))
                else:
                    old = self.get(type, obj['id'])
                    old.update(obj)

