import mutagen as mt
import wave

MUSIC_EXTENSIONS = {'mp3', 'm4a', 'wav', 'flac'}

class IncorrectFileTypeException(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)

class MusicFile:
    def __init__(self, pathname: str):
        # Extension of audio file, valid extensions in MUSIC_EXTENSIONS
        self.ext = None
        for ext in MUSIC_EXTENSIONS:
            if pathname.endswith(ext):
                self.ext = ext
        if not self.ext:
            raise IncorrectFileTypeException(f'Invalid file extension, must be one of {MUSIC_EXTENSIONS}.')

        self.pathname = pathname
        
        # Must contain 'title' and 'artist' keys after processing
        self.metadata = dict()
    
    def read_metadata(self):
        '''
        Read metadata of file at self.pathname
        - How this is run will vary by extension type
        '''
        pass

    def is_complete(self):
        '''
        Return True if self.metadata contains 'title' and 'artist' keys.
        '''
        return 'title' in self.metadata and 'artist' in self.metadata


if __name__ == '__main__':
    pass