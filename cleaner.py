from deluge_client import DelugeRPCClient
from config import config

client = DelugeRPCClient(
        config.delugehost.strip('"'),
        int(config.delugeport),
        config.delugeuser.strip('"'),
        config.delugepass.strip('"')
        )

client.connect()

def clean(id):
    client.call("core.remove_torrent", id, True)
