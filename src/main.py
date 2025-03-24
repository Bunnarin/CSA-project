import Interface
import Filter
import Operations
# init all the modules
interface = Interface()
filter = Filter()
operation = Operations()
# start
while True:
    filters = interface.get_input()
    files = filter.get_result(filters)
    if files == []:
        print("No files found. restarting application...")
        continue
    operations = interface.get_output()
    operation.operate(files,operations)
    continuation = input("Do you want to continue? (y/n): ")
    if continuation == "n": break

