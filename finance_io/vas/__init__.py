import importlib

from finance_io.vas.utils import getCurrentFuncName
from finance_io.config import CONF

def setupBackend(backendName=None):
    srcConn = None
    ruleEng = None
    backendName = backendName if backendName else 'wind'
    # search for wind.py and import then call wind.setupConn
    # search for rule file
    srcMod = \
        importlib.import_module(
            'finance_io.vas.backend.{modName}'.format(modName=backendName))
    return srcMod.setupConn(), srcMod.loadRuleEng()


class dataSource(object):
    def __init__(self, config=CONF):
        self.srcBackend = CONF["dataSource"]["name"]
        self.srcConn, self.rules = setupBackend(self.srcBackend)

    def getSector(self, **kwargs):
        res = None
        execParams = {}
        currentFuncName = getCurrentFuncName()
        for param_key in self.rules[currentFuncName]['params']:
            if kwargs[param_key]:
                execParams[param_key] = kwargs[param_key]
            else:
                raise
        execParams["mod"] = self.rules[currentFuncName]["mod"]
        execParams["func"] = self.rules[currentFuncName]["func"]

        if CONF["mod"] == "dev":
            res = execParams
        else:
            res = self.srcConn.execute(**execParams)

        return res
        
data_source = dataSource()
