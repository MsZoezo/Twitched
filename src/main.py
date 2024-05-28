import sys
import subprocess
import time
import webview
import multiprocessing

def open_chat(streamer):
    webview.create_window('Chat', "https://www.twitch.tv/popout/{}/chat?popout=".format(streamer))
    webview.start(private_mode=False)

def main():
    if len(sys.argv) < 2:
        print("Missing argument for the twitch channel! (silly)")
        return 1
    
    streamer = sys.argv[1]
    
    print("Loading mpv for twitch channel: {}".format(streamer))

    stream = subprocess.Popen(["mpv", "https://www.twitch.tv/{}".format(streamer)], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, shell=True)

    chat_process = multiprocessing.Process(target=open_chat, args=(streamer,))
    chat_process.start()

    while True:
        return_code = stream.poll()
        
        if return_code is not None:
            # Gotta make sure we kill the chat aswell >.>
            chat_process.kill()

            return return_code
        
        time.sleep(.3)