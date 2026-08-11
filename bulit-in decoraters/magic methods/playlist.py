class Playlist:
    def __init__(self,l=[]):
        self.l=l
    def valid_songs(self):
        if len(song)>4:
            n=len(song)
            return song[n-4:].lower()==".mp3"
        return False

