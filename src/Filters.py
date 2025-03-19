import os
import datetime
def get_all_files(path):
    try:
        files = []
        for item in os.listdir(path):
            # Skip hidden files and directories
            if item.startswith('.'): continue
            item_path = os.path.join(path, item)
            if os.path.isfile(item_path): files.append(item_path)
            else: files.extend(get_all_files(item_path))
        return files
    except Exception as e: return []

def filter_types(files, types):
    result_files = []
    for file in files:
        _, extension = os.path.splitext(file)
        if extension in types: result_files.append(file)
    return result_files

def filter_size(files, size, unit, mode):
    # convert to the correct unit
    if unit == "kb": size *= 1024
    elif unit == "mb": size *= 1024 * 1024
    elif unit == "gb": size *= 1024 * 1024 * 1024

    # filter the files
    if mode == "ls": files = [file for file in files if os.path.getsize(file) < size]
    elif mode == "gt": files = [file for file in files if os.path.getsize(file) > size]
    elif mode == "eq": files = [file for file in files if os.path.getsize(file) == size]
    return files

def filter_date(files, target_date_str, type, mode):
    target_date = datetime.datetime.strptime(target_date_str, "%Y-%m-%d").date()
    result_files = []
    for file in files:
        # get the date in yy-mm-dd format
        if type == "created": file_date = os.path.getctime(file)
        elif type == "modified": file_date = os.path.getmtime(file)
        elif type == "accessed": file_date = os.path.getatime(file)
        file_date = datetime.datetime.fromtimestamp(file_date).date()
        # filter the files
        if mode == "before" and file_date < target_date: result_files.append(file)
        elif mode == "after" and file_date > target_date: result_files.append(file)
        elif mode == "on" and file_date == target_date: result_files.append(file)
    return result_files

# in progress
def filter_wildcard(files, wildcard):
    pass
    return files

# test the code here
# files = get_all_files(".")
# print(files)
# print(filter_types(files, [".txt"]))
# print(filter_size(files, 1, "kb", "gt"))
# print(filter_date(files, "2025-03-12", "created", "on"))
