from http.server import HTTPServer, SimpleHTTPRequestHandler
from socketserver import TCPServer
from threading import Thread
import os, glob

from time import sleep # for testing

# goes to .\data, where .\ is the music-lib dir
DEFAULT_DIRECTORY = os.path.realpath(os.path.join(os.path.dirname(os.path.realpath(__file__)), r'..\data'))
DEFAULT_HOST = '127.0.0.1'
DEFAULT_PORT = '8000'


class Handler(SimpleHTTPRequestHandler):
    '''
    Handler for MusicServer, note that DIRECTORY is hard-coded in to be '../data'.
    - TODO: fix this, allow any directory to be used
    '''

    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DEFAULT_DIRECTORY, **kwargs)

class MusicServer:
    def __init__(self, host:str=DEFAULT_HOST, port:int=DEFAULT_PORT, directory:str=DEFAULT_DIRECTORY):
        self.port = str(port)
        self.host = host
        self.directory = DEFAULT_DIRECTORY # only uses curr default directory, to be fixed
        self.running = False

    def start_server(self) -> None:
        '''
        Starts a TCPServer at ``self.directory`` (default, and currently only, using localhost)
        - Access server using 'localhost:{self.port}'.
        - By default, directory opened is `./../data` on port 8000.
        '''
        self.httpd = TCPServer((self.host, int(self.port)), Handler)
        self.svr_thd = Thread(target=self.httpd.serve_forever, daemon=True)

        self.svr_thd.start()
        self.running = True

    def stop_server(self) -> None:
        '''
        Closes TCPServer, if it is running.
        '''
        if not self.running:
            return
        self.httpd.shutdown()
        self.running = False

    def get_files(self, exts=None) -> list[str]:
        '''
        Returns all files in ``self.directory`` (or in subdirectories of ``self.directory``) with extension exts.
        - If exts is None, return all files in ``self.directory``
        '''
        files = []
        for ext in exts:
            files.extend(glob.glob(rf"**\*.{ext}", root_dir=self.directory, recursive=True))
        
        return files


# testing purposes
if __name__ == '__main__':
    ms = MusicServer()
    print('Starting server...')
    ms.start_server()
    print('Started server')

    while True:
        x = input()
        if x == 'x':
            break

    print('Stopping server...')
    ms.stop_server()
    print('Stopped server')


    sleep(5)
    print('made it here')
