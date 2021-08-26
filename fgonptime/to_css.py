'''
layout.json -> filter.css
'''

import json
import collections

from .layout_to_filters import layout_to_filters

def make_selector(filter_type, filter_key):
    return f'[data-filter-{filter_type}]:not([data-filter-{filter_type}~="{filter_key}"]) [data-filter-key~="{filter_key}"]'

def load_filters():
    with open('layout.json', 'r', encoding='utf-8') as f:
        layout = json.load(f)
    return layout_to_filters(layout['filter_groups'])

def make_filter():
    filters = load_filters()
    css = ',\n'.join(make_selector(filter_type, filter_key) for filter_type, filter_keys in filters.items() for filter_key in filter_keys)
    css = css + ' {\n    visibility: collapse;\n}\n'
    return css

def export_css():
    css = make_filter()
    with open('public/css/filter.css', 'w', encoding='utf-8') as f:
        f.write(css)

def debug():
    print(make_filter())

if __name__ == '__main__':
    debug()

