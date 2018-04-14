#!/usr/bin/env sh
. "$( dirname "$0" )"/plexbot.conf

SOURCE=$1
CLIENT=$2
DEST_DIR=$plex

SICKRAGE_API=$srapi
COUCHPOTATO_API=$cpapi


if [ $CLIENT = "--nzbget" ]; then
    BASE=$nzb
elif [ $CLIENT = "--torrent" ]; then
    BASE=$torrents
elif [ $CLIENT = "--manual" ]; then
    BASE=$mdownloads
else
    echo "Error: Missing arguments"
fi


if [ $SOURCE = "--movies" ]; then
    echo "Processing Movies..."
    SOURCE_DIR="$BASE/Movies"
    CALLBACK="curl '$cpurl/api/$COUCHPOTATO_API/manage.update'"
elif [ $SOURCE = "--tv" ]; then
    echo "Processing Tv Shows..."
    SOURCE_DIR="$BASE/Shows"
    CALLBACK="curl '$srurl/api/$SICKRAGE_API?cmd=show.refresh&tvdbid={info.id}'"
elif [ $SOURCE = "--anime" ]; then
    echo "Processing Anime..."
    SOURCE_DIR="$BASE/Anime"
    CALLBACK=""
else
    echo "Error: Missing arguments"
    exit 1
fi


/usr/bin/filebot -script fn:amc --output $DEST_DIR --action copy -non-strict $SOURCE_DIR --conflict override --log-file $amclog --def subtitles=en,es --def excludeList=$amc --def clean=y --def unsorted=y --def extras=y --def seriesFormat="/home/plex/TV Shows/{n.replaceAll(/'/)}/Season {s.pad(2)}/{n} - {s00e00} - {t}" --def animeFormat="/home/plex/Anime/{n.replaceAll(/'/)}/Season {s.pad(2)}/{n} - {s00e00} - {t}" --def exec="$CALLBACK" --def minLengthMS=300000
