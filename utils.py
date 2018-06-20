import logging

from os import system
from shutil import rmtree
from config import config

scripts = config.scripts
FORMAT = '%(asctime)s:%(name)s:%(module)s:%(levelname)s: %(message)s'

def get_logger(name):
    loggging.basicConfig(level.logging.INFO, format=FORMAT)
    logger = logging.getLogger(name)

    try:
        handler = logging.handlers.SysLogHandler(address=(config.syslogaddr, config.syslogport))
        logger.addHandler(handler)
    except Exception:
        try:
            handler = logging.handlers.SysLogHandler(address='/dev/log')
            logger.addHandler(handler)
        except Exception:
            pass

    return logger

def categories(key):
    cats = {
        "movies": "--movies",
        "anime": "--anime",
        "tv": "--tv"
        }

    return cats[key]

def clean(download_dir):
    print("Removing: " + download_dir)
    rmtree(download_dir, ignore_errors=True)

def filebot(args, download_dir, delete=True):
    code = system(scripts + "/plexbot.sh " + args)
    if code is 0:
        if delete:
            clean(download_dir)
        return True

    else:
        return False
