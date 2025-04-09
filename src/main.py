import interface
import filter_csb as filter
import operation
while True:
    filter_params = interface.get_filters()
    files = filter.get_result(filter_params)
    if files == []:
        print("No files found. restarting application...")
        continue
    
    operation_params = interface.get_operations()
    operation.operate(files, operation_params)
    continuation = input("Do you want to continue? (y/n): ")
    if continuation.lower() == "n": break

