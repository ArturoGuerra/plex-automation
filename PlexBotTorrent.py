#!/usr/bin/env python3.6
from os import environ, system
from sys import exit
from utils import filebot, categories
from config import config

base = config.torrents.strip('"')
torrent_dir = environ.get("TR_TORRENT_DIR")

if torrent_dir == base + "/Movies":
    category = "movies"
elif torrent_dir == base + "/Shows":
    category = "tv"
else:
    print("Invalid Torrent")
    exit(0)

cat = categories(category)
args = cat + " --torrent"

filebot(args, None, False)
system(config.scripts + '/torrentcleaner.js')
print("Done :():")
exit(0)
