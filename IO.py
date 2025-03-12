# must handle invalid input

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
    'date': ('2020-01-01-hh-mm', 'c/m/a', 'before/on/after'),
    'wildcard': 'hello*'
}

def get_output():
    print('''
    operations:
        1.move
        2.copy
        3.delete
        4.find and replace
    ''')
    return actions
# example actions:
actions = {
    'type': 'copy',
    'parameter': 'path, None, (find, replace)'
}