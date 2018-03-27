from os import system
from shutil import rmtree
from config import config

scripts = config.scripts

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
        print("Finished :)")
        return True

    else:
        print("Error :(")
        return False
