import requests
from getpass import getpass
import json

api_url = "https://suap.ifrn.edu.br/api/"

user = input("digite a matricula: ")
password = getpass(prompt="senha: ")

data = {"username":user,"password":password}

response = requests.post(api_url+"v2/autenticacao/token/", json=data)
token = response.json()["access"]
#print(response.json())

headers = {
    "Authorization": f'Bearer {token}'
}

print(headers)

ano_letivo = input("Digite o ano letivo: ")
periodo = input("digite o periodo: ")
response = requests.get(api_url+f"v2/minhas-informacoes/boletim/{ano_letivo}/{periodo}/", headers=headers).json()

#print(response.text)
#print(response)

for disciplina in response:
    print(f"Média {disciplina['mediadadisciplina']} - {disciplina['disciplina']}")