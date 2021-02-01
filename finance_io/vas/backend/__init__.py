from finance_io.config import CONF
from finance_io.utils.loadtools import importMod

def setupBackend(backendName):
    return importMod(backendName, __name__).proxy

class srcProxy(object):

    def __init__(self):
        pass

    def execute(self, **kwargs):
        res = None
        paramTemp = self.reqRend(**kwargs)
        if CONF['dataSource']['mod'] == "dev":
            res = paramTemp
        else:
            res = self._execute(paramTemp)
        return res

    def _execute(self, sec=None, func=None, **kwargs):
        pass

    def reqRend(self, sec=None, func=None, **kwargs):
        pass
