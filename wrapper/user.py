# cli.py

import user_wrapper as users
import requests

def listar_usuarios():
    all_users = users.list()
    for user in all_users:
        print(f"ID: {user['id']}, Nome: {user['name']}, Username: {user['username']}")

def exibir_usuario(id):
    user = users.read(id)
    if user:
        print(user)
    else:
        print("Usuário não encontrado.")

def criar_usuario():
    name = input("Nome: ")
    username = input("Username: ")
    email = input("Email: ")
    new_user = users.create(name, username, email)
    print("Usuário criado com sucesso:", new_user)

def atualizar_usuario(id):
    name = input("Novo Nome (deixe em branco para manter): ")
    username = input("Novo Username (deixe em branco para manter): ")
    email = input("Novo Email (deixe em branco para manter): ")
    updated_user = users.update(id, name, username, email)
    if updated_user:
        print("Usuário atualizado com sucesso:", updated_user)
    else:
        print("Usuário não encontrado.")

def deletar_usuario(id):
    users.delete(id)
    print("Usuário deletado com sucesso.")

def main():
    while True:
        print("\nMenu:")
        print("1. Listar todos os usuários")
        print("2. Exibir detalhes de um usuário")
        print("3. Criar novo usuário")
        print("4. Atualizar um usuário")
        print("5. Deletar um usuário")
        print("6. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            listar_usuarios()
        elif opcao == "2":
            id = int(input("ID do usuário: "))
            exibir_usuario(id)
        elif opcao == "3":
            criar_usuario()
        elif opcao == "4":
            id = int(input("ID do usuário: "))
            atualizar_usuario(id)
        elif opcao == "5":
            id = int(input("ID do usuário: "))
            deletar_usuario(id)
        elif opcao == "6":
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
