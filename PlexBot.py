#!/usr/bin/env python

###########################################
### NZBGET POST-PROCESSING SCRIPT       ###

# PlexBot
#
# This is script uses filebot and python to do shit
#

### NZBGET POST-PROCESSING SCRIPT       ###
###########################################

from os import environ
from sys import exit
from utils import categories, filebot, get_logger

logger = get_logger('PlexBotNZB')

logger.info("Running PlexBot")

mode = ' --nzbget'
status = environ.get("NZBPP_TOTALSTATUS")
category = environ.get("NZBPP_CATEGORY")
download_dir = environ.get("NZBPP_DIRECTORY")
POST_ERROR=94
POST_SUCCESS=93

cat = categories(category)
args = cat + mode

def check():
    if status == "SUCCESS":
        logger.info("Downloaded :)")
        if filebot(args, download_dir):
            exit(POST_SUCCESS)
        else:
            exit(POST_ERROR)

    elif status == "FAILURE":
        logger.info("Download Failed")
        exit(POST_ERROR)

    else:
        exit(POST_SUCCESS)

check()
