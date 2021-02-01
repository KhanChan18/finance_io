import os
import yaml

def readYAML(filePath):
    content = None
    with open(filePath, 'r') as inFile:
        content = yaml.load(inFile, Loader=yaml.FullLoader)
    return content
