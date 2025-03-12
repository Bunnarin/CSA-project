def get_input():
    # get a directory
    print('''
    filter by:
        1.type
        2.size
        3.date
        4.wildcard
    ''')
    return filters
# example filters:
filters = {
    'path': 'C:/Users/',
    'types': ['txt', 'pdf'],
    'size': (100, 'kb', 'lt/eq/gt'),
    'date': ('yyyy-mm-dd', 'c/m/a', 'before/on/after'),
    'wildcard': 'hello*'
}
# c = creation, m = modified, a = access