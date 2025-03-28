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

    def get_output(self):
        print('''
        operations:
            1.move
            2.copy
            3.delete
            4.find and replace
        ''')
        choice = int(input("Enter any operations you want to operate between 1 and 4:  "))

        if choice == 1:
            move_to = input("Where do you want to move to? ")
            actions = {'Type' : 'move','parameter' : move_to}
            print(f"Moved to {move_to}")
        elif choice == 2:
            copy = input("Copy to where?  ")
            actions = {'Type': 'copy', 'parameter':copy}
            print(f"Done copied to {copy}")
        elif choice == 3:
            actions = {'Type': 'Delete', 'parameter': None}
        elif choice == 4:
            find = input("Enter the file you want to find: ")
            replace = input("Replace with what?: ")
            actions = {'Type':'find_replace', 'parameter': (find, replace)}
        else:
            print("Enter only any of these 4 operations: ")
            choice = int(input("Enter: "))

        return actions