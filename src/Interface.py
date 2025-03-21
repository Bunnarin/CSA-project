class Interface:
    def __init__(self): pass

    def get_input(self):
        # get a directory
        print('''
        filter by:
            1.type
            2.size
            3.date
            4.wildcard
        ''')
        filters = {}
        return filters

    # thanou
    def get_output(self, files):
        if not files: 
            print("no files were selected with the input filters. exiting.")
            return
        print('''
        operations:
            1.move
            2.copy
            3.delete
            4.find and replace
        ''')
        actions = {}
        return actions
# example result:
actions = {
    'type': 'copy/move/delete/find_replace',
    'params': 'path/None/(find, replace)'
}