import interface
import filter
import operation
while True:
    filter_params = interface.get_input()
    files = filter.get_result(filter_params)
    if files == []:
        print("No files found. restarting application...")
        continue
    operation_params = interface.get_output()
    operation.operate(files, operation_params)
    continuation = input("Do you want to continue? (y/n): ")
    if continuation == "n": break

