from Crypto.Hash import SHA256
from threading import Thread
import os
import sys
import random
import subprocess

args = sys.argv
diff = float(subprocess.check_output(("curl " + args[1] + "/get_mine -s").split(" ")))
os.system("curl " + args[1] + "/new_mine -s > /dev/null")

def thread():
    while True:
        r = str(hex(random.randint(1, (2**32)))[2:])
        Hash = SHA256.new()
        Hash.update(r)
        if int(Hash.hexdigest(), 16) < (diff):
            os.system("curl " + sys.argv[1] + "/submit*" + r + "*" + sys.argv[2] + ">/dev/null")

cores = float(raw_input("enter cores to mine on: "))
n = 0

while n<cores:
    Thread(target=thread).start()
    n+=1

print("Mining... ")
