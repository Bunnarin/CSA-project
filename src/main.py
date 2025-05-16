import Interface
import Filter
import operation
while True:
    filter_params = Interface.get_filters()
    files = Filter.get_result(filter_params)
    if files == []:
        print("No files found. restarting application...")
        continue
    
    operation_params = Interface.get_operations()
    operation.operate(files, operation_params)
    continuation = input("Do you want to continue? (y/n): ")
    if continuation.lower() == "n": break

