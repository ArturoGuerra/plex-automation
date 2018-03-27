#!/usr/bin/env node
const Transmission = require('transmission');
const fs = require('fs');
const config = require('./transmission.json');

transmission = new Transmission(config[0])

function deleteTorrent(id){
    transmission.remove(id, true, function(err, result){
        if (err){
            console.log(err);
        }
    });
}

async function checkFile(file) {
    let d = fs.readFileSync(config[1].amc, 'utf8');
    return d.indexOf(file) !== -1
}

async function getAllActiveTorrents(){
    transmission.get(async function(err, result){
    console.log('\n--------------------------')
    console.log("Starting TorrentCleaner...")
    if (err){
        console.log(err);
    }
    else {
        for (var i=0; i < result.torrents.length; i++){
            let del = false
            let files = result.torrents[i].files
            let fpath = result.torrents[i].downloadDir
            for (let i =0; i < files.length; i++) {
                del = await checkFile(fpath + '/' + files[i].name);
                if (del) {break;};

            }
            if (del) {
                console.log("Deleting " + result.torrents[i].name);
                deleteTorrent(result.torrents[i].id);
            } else {
                console.log("Torrent " + result.torrents[i].name + " is still in use");
            }
        }
    }
    console.log('--------------------------\n')
    });
}

getAllActiveTorrents()
