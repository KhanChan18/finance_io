import importlib

from finance_io.config import CONF
from finance_io.utils.misc import getCurrentFuncName
from finance_io.vas.backend import setupBackend

class dataSource(object):
    def __init__(self, config=CONF):
        self.srcBackend = CONF["dataSource"]["name"]
        self.srcProxy = setupBackend(self.srcBackend)

    def getSector(self, **kwargs):
        res = None
        currentFuncName = getCurrentFuncName()
        execParams = {
            "call": currentFuncName,
            "mod": self.srcProxy.protocols[currentFuncName]['mod'],
            "func": self.srcProxy.protocols[currentFuncName]['func'],
        }
        for param_key in self.srcProxy.protocols[currentFuncName]['params']:
            if kwargs[param_key]:
                execParams[param_key] = kwargs[param_key]
            else:
                raise
        return self.srcProxy.execute(**execParams)
        
data_source = dataSource()
