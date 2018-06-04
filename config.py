from os import path
from sys import argv

class Config:
    def __init__(self):
        script_path = path.dirname(path.realpath(argv[0]))
        rawconfig = open(script_path + '/plexbot.conf', 'r').read()
        vals = rawconfig.split('\n')
        for val in vals:
            try:
                p = val.split("=")
                setattr(self.__class__, p[0], p[1])
            except Exception as e:
                pass

config = Config()
