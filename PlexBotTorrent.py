#!/usr/bin/env python3.6
from os import environ, system
from sys import exit, argv
from utils import filebot, categories
from config import config
from cleaner import clean
from syslog import syslog

syslog("Starting PlexBotTorrent...")
base = config.torrents.strip('"')
torrent_id = argv[1]
torrent_name = argv[2]
torrent_dir = argv[3]
syslog("Torrent ID: " + torrent_id)

if torrent_dir == base + "/Movies":
    category = "movies"
elif torrent_dir == base + "/Shows":
    category = "tv"
else:
    syslog("Invalid Torrent")
    exit(0)

cat = categories(category)
args = cat + " --torrent"
syslog("FileBot Args: " + args)
filebot(args, None, False)
clean(torrent_id);
syslog("Done :():")
exit(0)
