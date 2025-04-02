import os
import datetime

def get_result(filters): 
    files = get_all_files(filters["path"])
    if filters["types"]: files = filter_types(files,filters["types"])
    if filters["size"]: files = filter_size(files,filters["size"])
    if filters["date"]: files = filter_date(files,filters["date"])
    if filters["wildcard"]: files = filter_wildcard(files,filters["wildcard"])
    return files

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

def filter_size(files, params):
    size, unit, mode = params
    # convert to the correct unit
    if unit == "kb": size *= 1024
    elif unit == "mb": size *= 1024 * 1024
    elif unit == "gb": size *= 1024 * 1024 * 1024

    # filter the files
    if mode == "lt": return [file for file in files if os.path.getsize(file) < size]
    elif mode == "gt": return [file for file in files if os.path.getsize(file) > size]
    elif mode == "eq": return [file for file in files if os.path.getsize(file) == size]

def filter_date(files, params):
    target_date_str, type, mode = params
    target_date = datetime.datetime.strptime(target_date_str, "%Y-%m-%d").date()
    result_files = []
    for file in files:
        # get the date in yy-mm-dd format
        if type == "c": file_date = os.path.getctime(file)
        elif type == "m": file_date = os.path.getmtime(file)
        elif type == "a": file_date = os.path.getatime(file)
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

# test here
# filters = {
#     'path': '.',
#     'types': [".py"],
#     'size': (100, 'kb', 'lt'),
#     'date': ('2025-01-01','c','after'),
#     'wildcard': None
# }
# filter = Filter(filters)
# files = filter.get_result()
# print(files)
