from musiclib_server import MusicServer
from mongo_server import MongoDBServer
import requests

from music_metadata import MUSIC_EXTENSIONS

from time import sleep

# this file needs to be renamed.... later





def categorize_music(msvr: MusicServer):
    files = msvr.get_files(MUSIC_EXTENSIONS)
    


if __name__ == '__main__':
    msvr = MusicServer()
    mdbsvr = MongoDBServer()

    msvr.start_server()
    categorize_music(msvr)

    
    



