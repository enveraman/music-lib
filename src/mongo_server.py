import pymongo

from time import sleep

import pymongo.database

DEFAULT_PORT = 27017
DEFAULT_DB_NAME = "music-lib"

class MongoDBServer:
    def __init__(self, port:int = DEFAULT_PORT, db_name:str = DEFAULT_DB_NAME) -> None:
        self.port = port
        self.db_name = db_name
        self.running = False

    def start_server(self) -> pymongo.Database:
        '''
        Starts a localhost MongoDB server with database name ``self.db_name``, returns Database created
        - Access server using 'mongodb://localhost:{port}'.
            - *Note:* Requires MongoDBCompass to view in GUI.
        - By default, opened on port 27017.
        '''
        self.client = pymongo.MongoClient(f"mongodb://localhost:{self.port}/")
        self.db = self.client[self.db_name]
        self.running = True
        return self.db
        
    def stop_server(self) -> None:
        '''
        Closes MongoDB server, if it is running. Otherwise, do nothing.
        '''
        if self.running:
            self.client.close()
        


if __name__ == "__main__":
    mdb = MongoDBServer()
    
    print('Starting server...')
    mdb.start_server()
    print('Started server')

    sleep(2)

    print('Stopping server...')
    mdb.stop_server()
    print('Stopped server')