import os
# example
files = [
    "D:\CS\CSA\IO.py",
    "D:\CS\CSA\filters.py",
    "D:\CS\CSA\Operations.py",
    "D:\CS\CSA\main.py",
]
actions = {
    'type': 'copy',
    'parameter': 'path, None, (find, replace)'
}
def operate(files, operations):
    params = operations["params"]
    if operations["type"] == "move": move(files, params)
    elif operations["type"] == "copy": copy(files, params)
    elif operations["type"] == "delete": delete(files)
    elif operations["type"] == "find_replace": find_replace(files, params)
def move(files, destination):
    pass
def copy(files, destination):
    pass
def delete(files):
    pass
def find_replace(files, params):
    find, replace = params
    pass