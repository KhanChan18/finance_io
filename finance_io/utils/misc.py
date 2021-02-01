import inspect
import os

def genPath(path, prefix=None, absPath=True):
    """This function should be platform-independent.
    """
    res = ''
    if absPath:
        res = os.path.join(prefix, path)
    else:
        res = path
    return res

def getCurrentFuncName():
    return inspect.stack()[1][3]
