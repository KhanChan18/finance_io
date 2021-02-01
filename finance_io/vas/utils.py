import inspect

def getCurrentFuncName():
    return inspect.stack()[1][3]
