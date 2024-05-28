import sys
import subprocess
import time



def main():
    if len(sys.argv) < 2:
        print("Missing argument for the twitch channel! (silly)")
        return 1
    
    streamer = sys.argv[1]
    
    print("Loading mpv for twitch channel: {}".format(streamer))

    stream = subprocess.Popen(["mpv", "https://www.twitch.tv/{}".format(streamer)], stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT, shell=True)

    while True:
        return_code = stream.poll()
        
        if return_code is not None:
            return return_code
        
        time.sleep(.3)