import pypresence
from datetime import timedelta
from datetime import datetime
from time import time as timer
import time
import psutil
import socket
import sys
def launch(client_id:str,pipe:int):
    presence = pypresence.Presence(client_id=client_id,pipe=pipe)

    times = timer()

    while True:
        try:
            presence.connect()
        except:
            print("Could not connect to Discord, retrying in 5 seconds")
            time.sleep(5)
        else:
            break
    while True:
        presence.clear()
        detail = f"""
        CPU: {int(psutil.cpu_percent())}%
        RAM: {int(psutil.virtual_memory().percent)}%
        Disk: {int(psutil.disk_usage('/').percent)}%
        Boot time: {timedelta(seconds=int(time.time() - times))}
        Script Started for: {datetime.now() - datetime.fromtimestamp(times)}
        """
        buttons = [{"label":"Want this? Click to Download!","url":"https://github.com/dumb-stuff/presence-stats"}]
        presence.update(details=f"System Info of {socket.gethostname()}",state=detail,start=times,buttons=buttons)
        time.sleep(1)
        print("Updated Presence")

def launcharg(client_id:str = 904942886070673479,pipe:int = 0):
    try:
        client_id = sys.argv[1]
    except Exception:
        pass
    try:
        pipe = sys.argv[2]
    except Exception:
        pass
    presence = pypresence.Presence(client_id=client_id,pipe=pipe)

    times = timer()

    while True:
        try:
            presence.connect()
        except:
            print("Could not connect to Discord, retrying in 5 seconds")
            time.sleep(5)
        else:
            break
    while True:
        detail = f"""CPU: {int(psutil.cpu_percent())}%\nRAM: {int(psutil.virtual_memory().percent)}%\nDisk: {int(psutil.disk_usage('/').percent)}%\n\nStarted time: {timedelta(seconds=int(time.time() - times))}
            """
        print(len(detail))
        buttons = [{"label":"Want this? Click to Download!","url":"https://github.com/dumb-stuff/presence-stats"}]
        presence.update(details=f"System Info of {socket.gethostname()}",state=detail,start=times,buttons=buttons)
        time.sleep(1)
        print("Updated Presence")
