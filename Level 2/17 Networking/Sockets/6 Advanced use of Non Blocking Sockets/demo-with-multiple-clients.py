import subprocess
import time
from subprocess import Popen
from threading import Thread


def startServer():
    # server keeps running, so start in on a separate thread 
    params = "python server.py".split()
    serverThread = Thread(target=subprocess.call, args=(params,))
    serverThread.start()


def startClients(n):
    for i in range(n):
        cmd = "python client.py {0}".format(i)
        p = Popen(cmd.split())  # clients run asynchronously


startServer()
time.sleep(5)
startClients(10)
