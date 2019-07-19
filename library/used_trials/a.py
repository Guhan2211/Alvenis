import time
import sys
from threading import *
from getchannel import obj

def draw():
    del sys.modules['getchannel']
    from getchannel import obj
    #print(obj.info)
    #print("XYZ")
    
while True:

        draw()
        time.sleep(15)

        #draw()

        #del sys.modules['getchannel']




    # create thread
    #t = Timer(5.0, draw)
 
    # start thread after 10 seconds
    #t.start()
