import os
# example
files = [
    "D:\CS\CSA\IO.py",
    "D:\CS\CSA\filters.py",
    "D:\CS\CSA\ops_params.py",
    "D:\CS\CSA\main.py",
]
actions = {
    'type': 'copy',
    'parameter': 'path, None, (find, replace)'
}
def operate(files, ops_params):
    params = ops_params["params"]
    if ops_params["type"] == "move": move(files, params)
    elif ops_params["type"] == "copy": copy(files, params)
    elif ops_params["type"] == "delete": delete(files)
    elif ops_params["type"] == "find_replace": find_replace(files, params)
def move(files, destination):
    pass
def copy(files, destination):
    pass
def delete(files):
    pass
def find_replace(files, params):
    find, replace = params
    pass