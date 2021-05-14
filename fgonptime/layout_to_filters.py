import collections

def layout_to_filters(layout):
    filters = collections.defaultdict(list)
    for filter_group in layout:
        for filter_type, filter_keys in filter_group.items():
            filters[filter_type].extend(filter_keys)
    return filters
