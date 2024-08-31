import requests
from requests.auth import HTTPBasicAuth
from getpass import getpass

url = "https://api.github.com/user/"

def seguindo(username):
    return f"https://api.github.com/user/following/{username}"

def seguidores():
    return "https://api.github.com/user/followers"

def listadeseguidores(login, password):
    response = requests.get(seguidores(), auth=HTTPBasicAuth(login, password))

    if response.status_code == 200:
        followers = response.json()
        for i, follower in enumerate(followers):
            print(f"{i} - {follower['login']}")
    else:
        print(f"Requisição falhou com o código de status {response.status_code} - {response.text}")

def seguir(login, password):
    username = input('Digite o nome do usuário que deseja seguir: ')
    response = requests.put(seguindo(username), auth=HTTPBasicAuth(login, password))

    if response.status_code == 204:
        print(f'Seguindo {username} com sucesso!')
    else:
        print(f"Erro ao seguir {username}: {response.status_code} - {response.text}")

def parardeseguir(login, password):
    username = input("Digite o nome do usuário que deseja parar de seguir: ")
    response = requests.delete(seguindo(username), auth=HTTPBasicAuth(login, password))

    if response.status_code == 204:
        print(f'Parou de seguir {username} com sucesso!')
    else:
        print(f"Erro ao parar de seguir {username}: {response.status_code} - {response.text}")

def login_and_token():
    login = input("Digite seu login: ")
    password = getpass("")
    return login, password

def menu():
    username, password = login_and_token()

    while True:
        print(f"Logado como {username}\n")

        print('-' * 40)
        print('1 - Lista de seguidores')
        print('2 - Seguir um usuário')
        print('3 - Parar de seguir um usuário')
        print('4 - Sair')
        print('-' * 40)

        opcao = input('Digite uma opção: ')

        if opcao == '1':
            listadeseguidores(username, password)
        
        elif opcao == '2':
            seguir(username, password)

        elif opcao == '3':
            parardeseguir(username, password)

        elif opcao == '4':
            print("Saindo...")
            break
        
        else:
            print("Opção inválida. Tente novamente.")

menu()
