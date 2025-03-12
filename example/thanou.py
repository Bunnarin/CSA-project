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