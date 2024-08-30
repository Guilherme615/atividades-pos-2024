import requests
from requests.auth import HTTPBasicAuth
from getpass import getpass

user = input("user: ")
password = getpass("")
  
response = requests.get('https://api.github.com/user/followers', auth = HTTPBasicAuth('Guilherme615', password))
  

seguidores = response.json()

for i, seguidor in enumerate(seguidores, start=1):
    print(f"{i} - {seguidor['login']}")

print(response.status_code)