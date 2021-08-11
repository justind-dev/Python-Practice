class StreamAlreadyOpenError(Exception):
    pass

class StreamNotOpenError(Exception):
    pass

class Stream():
    def __init__(self):
        self.opened = False
    
    def open(self):
        if self.opened:
            raise StreamAlreadyOpenError("Stream already opened")
        self.opened = True

    def close(self):
        if not self.opened:
            raise StreamNotOpenError("No stream open")
        self.opened = False

class FileStream(Stream):
    def read(self):
        print("Reading data from a file...")

class NetworkStream(Stream):
    def read(self):
        print("Reading data from the network...")

ns = NetworkStream()
fs = FileStream()
ns.open()
fs.open()

ns.close()
fs.close()

#erroneous close
ns.close()

