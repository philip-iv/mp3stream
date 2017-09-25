import requests
import time

class mp3stream:
    def __init__(self, url):
        self.url = url
        
    def write(self, file_name, duration):
        if duration < 0:
            return
        endtime = time.time() + duration
        r = requests.get(self.url, stream=True)
        with open(file_name, 'wb') as f:
            for block in r.iter_content(1024):
                f.write(block)
                if time.time() > endtime:
                    return
        
    def get_stream_name(self):
        r = requests.get(self.url, stream=True)
        stream_name = r.headers['icy-name']
        return stream_name