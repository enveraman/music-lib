from http.server import HTTPServer, SimpleHTTPRequestHandler
from threading import Thread
import os

from time import sleep # for testing

# goes to .\..\data, where .\ is the music-lib dir
DIRECTORY = os.path.realpath(os.path.join(os.path.dirname(os.path.realpath(__file__)), '..\data'))
DEFAULT_PORT = 8000

class Handler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

class MusicServer:
    def __init__(self, port=DEFAULT_PORT, verbose=False):
        self.port = port
        self.verbose = verbose
        self.running = False

    def start_server(self):
        '''
        Starts a localhost file server at directory.
        - Access server using 'localhost:{port}'.
        - By default, directory opened is `./../data` on port 8000.
        '''
        self.httpd = HTTPServer(('localhost', self.port), Handler)
        self.svr_thd = Thread(target=self.httpd.serve_forever, daemon=True)
        
        self.svr_thd.start()
        self.running = True

    def stop_server(self):
        if not self.running:
            return
        self.httpd.shutdown()
        self.running = False


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
