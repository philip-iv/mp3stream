# About

Timeshift is a small python lib to save streaming mp3 radio. The primary intended
use is to timeshift internet radio, but other applications are possible.

# Requirements

Timeshift depends on `requests` to download streams and get radio metadata.

# Use

The `mp3stream` class is used to download and get info on a stream. A new stream
object should be created for each stream source. A basic example:

```
from mp3stream import mp3stream
import time
import os

stream_url = 'http://17273.live.streamtheworld.com/WUTCFM.mp3'
stream = mp3stream(stream_url)
stream_name = stream.get_stream_name()
file_name = '%s_%d.mp3' % (stream_name, time.time())

stream.write(os.path.join('audio', file_name), 10)
```