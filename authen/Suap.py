import requests
from getpass import getpass
import json

api_url = "https://suap.ifrn.edu.br/api/"

user = input("Digite a matrícula: ")
password = getpass(prompt="Senha: ")

data = {"username": user, "password": password}

response = requests.post(api_url + "v2/autenticacao/token/", json=data)

if response.status_code == 200:
    token = response.json().get("access")
    print("Autenticação bem-sucedida!")
else:
    print(f"Falha na autenticação: {response.status_code} - {response.text}")
    exit()

headers = {
    "Authorization": f'Bearer {token}'
}

ano_letivo = input("Digite o ano letivo: ")
periodo = input("Digite o período: ")

response = requests.get(api_url + f"v2/minhas-informacoes/boletim/{ano_letivo}/{periodo}/", headers=headers)

if response.status_code == 200:
    boletim = response.json()
    for disciplina in boletim:
        print(f"Média {disciplina['media_final']} - {disciplina['disciplina']}")
else:
    print(f"Erro ao obter o boletim: {response.status_code} - {response.text}")
