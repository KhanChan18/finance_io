import os
import yaml

from .api import setupConn, execute


def loadRuleEng():
    with open(os.path.abspath(os.path.join("vas", "backend", "wind", "rules", "rules.yml")), 'r') as inFile:
        res = yaml.load(inFile, Loader=yaml.FullLoader)
    return res

