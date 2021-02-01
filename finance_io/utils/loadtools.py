import importlib

def importMod(modName, package=''):
    """Dynamically Mod load
    """
    modPath = '.'.join([package, modName])
    return importlib.import_module(modPath)
    

def importObj(objName, modName, modPath):
    """Dynamically Object load
    """
    mod = importMod(modName, modPath)
    return mod.get(objName)
