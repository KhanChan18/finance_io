import json
import yaml

CONF_PATH = "conf/conf-sample.yml"

def loadConfig():
    with open(CONF_PATH, "r") as inFile:
        return yaml.load(inFile, Loader=yaml.FullLoader)['globalConfig']

CONF = loadConfig()
