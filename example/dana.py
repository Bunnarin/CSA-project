def get_input():
    filters = {'types': [], 'size': None, 'date': None, 'wildcard': None}
    path = input("Enter the path to search: ")
    filters['path'] = path.strip()
    while True:
        print('''
        Filter by:
            1. Type
            2. Size
            3. Date
            4. Wildcard
            5. Done
        ''')
        user_choice = input("Enter your choice(1/2/3/4/5): ")

        if user_choice == "1":
            while True:
                file_type = input("Enter a type: ")
                filters['types'].append(file_type)
                more_choice = input("Do you want to add more types? yes/no: ")
                if more_choice.lower() == "no":
                    break

        elif user_choice == "2":
            while True:
                size = input("Enter a size: ")
                if not size.isdigit():
                    print("Error: Please enter a valid number for size.")
                    continue

                size = int(size)
                unit = input("Enter a unit (kb/mb/gb): ").lower()
                if unit not in ['kb', 'mb', 'gb']:
                    print("Error: Please enter a valid unit (kb/mb/gb).")
                    continue

                condition = input("Less than, Equal, or Greater than (lt/eq/gt): ").lower()
                if condition not in ['lt', 'eq', 'gt']:
                    print("Error: Please enter a valid condition (lt/eq/gt).")
                    continue

                filters['size'] = (size, unit, condition)
                break

        elif user_choice == "3":
            while True:
                dateStr = input("Enter a date (yyyy-mm-dd): ")
                year, month, day = map(int, dateStr.split('-'))
                if 1 > month > 12 or 1 > day > 31 or year < 1970: 
                    print("Error: Please enter a valid date in the format yyyy-mm-dd.")
                    continue

                date_condition = input("before, on, or after: ").lower()
                if date_condition not in ['before', 'on', 'after']:
                    print("Error: Please enter a valid condition (before/on/after).")
                    continue

                filters['date'] = (dateStr, date_condition)
                break

        elif user_choice == "4":
            wildcard = input("Enter a wildcard: ")
            wildcard_chars = ['*', '?', '[', ']']
            if not any(char in wildcard for char in wildcard_chars):
                print("Error: Please enter a valid wildcard pattern,", wildcard_chars)
                continue

            filters['wildcard'] = wildcard

        elif user_choice == "5":
            break   

        else:
            print("Error: Invalid choice. Please select a valid option.")

    return filters

filters = get_input()
print(filters)