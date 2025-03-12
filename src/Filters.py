import os
import datetime
def get_all_files(path):
    try:
        files = []
        for item in os.listdir(path):
            if item.startswith('.'):  # Skip hidden files and directories
                continue
            full_path = os.path.join(path, item)
            if os.path.isfile(full_path):
                files.append(full_path)
            else:
                # Recursively call the function for subdirectories
                files.extend(get_all_files(full_path))
        return files
    except Exception as e:
        print(f"Error: {e}")
        return []

def filter_types(files, types):
    result_files = []
    for file in files:
        _, extension = os.path.splitext(file)
        if extension in types:
            result_files.append(file)
    return result_files

def filter_size(files, size, unit, mode):
    # convert to the correct unit
    if unit == "kb":
        size = size * 1024
    elif unit == "mb":
        size = size * 1024 * 1024
    elif unit == "gb":
        size = size * 1024 * 1024 * 1024

    # filter the files
    if mode == "ls":
        files = [file for file in files if os.path.getsize(file) < size]
    elif mode == "gt":
        files = [file for file in files if os.path.getsize(file) > size]
    elif mode == "eq":
        files = [file for file in files if os.path.getsize(file) == size]
    return files

def filter_date(files, target_date_str, type, mode):
    target_date = datetime.datetime.strptime(target_date_str, "%Y-%m-%d").date()
    result_files = []
    for file in files:
        # get the date
        if type == "created":
            file_date = os.path.getctime(file)
        elif type == "modified":
            file_date = os.path.getmtime(file)
        elif type == "accessed":
            file_date = os.path.getatime(file)
        # convert the date to yyyy-mm-dd
        file_date = datetime.datetime.fromtimestamp(file_date).date()
        # filter the files
        if mode == "before":
            if file_date < target_date:
                result_files.append(file)
        elif mode == "after":
            if file_date > target_date:
                print(file)
                result_files.append(file)
                continue
        elif mode == "on":
            if file_date == target_date:
                result_files.append(file)
    return result_files

# solo 2: vutha
def filter_wildcard(files, wildcard):
    ...
    return files

files = get_all_files(".")

# test the code here
# print(files)
# print(filter_types(files, [".txt"]))
# print(filter_size(files, 1, "kb", "gt"))
# print(filter_date(files, "2025-03-12", "created", "on"))
