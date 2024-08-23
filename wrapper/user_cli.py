import json

# Dados dos usuários
users = [
    {
        "id": 1,
        "name": "Leanne Graham",
        "username": "Bret",
        "email": "Sincere@april.biz",
        "address": {
            "street": "Kulas Light",
            "suite": "Apt. 556",
            "city": "Gwenborough",
            "zipcode": "92998-3874",
            "geo": {
                "lat": "-37.3159",
                "lng": "81.1496"
            }
        },
        "phone": "1-770-736-8031 x56442",
        "website": "hildegard.org",
        "company": {
            "name": "Romaguera-Crona",
            "catchPhrase": "Multi-layered client-server neural-net",
            "bs": "harness real-time e-markets"
        }
    },
    # [Outros usuários aqui...]
]

# Função para listar todos os usuários
def listar_usuarios():
    for user in users:
        print(f"ID: {user['id']}, Nome: {user['name']}, Username: {user['username']}")

# Função para exibir detalhes de um usuário específico
def exibir_usuario(id):
    user = next((user for user in users if user['id'] == id), None)
    if user:
        print(json.dumps(user, indent=4))
    else:
        print("Usuário não encontrado.")

# Função para criar um novo usuário
def criar_usuario():
    new_id = max(user["id"] for user in users) + 1
    name = input("Nome: ")
    username = input("Username: ")
    email = input("Email: ")
    # Dados simplificados para o exemplo
    new_user = {
        "id": new_id,
        "name": name,
        "username": username,
        "email": email,
        "address": {},
        "phone": "",
        "website": "",
        "company": {}
    }
    users.append(new_user)
    print("Usuário criado com sucesso.")

# Função para atualizar um usuário existente
def atualizar_usuario(id):
    user = next((user for user in users if user['id'] == id), None)
    if user:
        user['name'] = input(f"Nome ({user['name']}): ") or user['name']
        user['username'] = input(f"Username ({user['username']}): ") or user['username']
        user['email'] = input(f"Email ({user['email']}): ") or user['email']
        print("Usuário atualizado com sucesso.")
    else:
        print("Usuário não encontrado.")

# Função para deletar um usuário
def deletar_usuario(id):
    global users
    users = [user for user in users if user['id'] != id]
    print("Usuário deletado com sucesso.")

# Função principal para a CLI
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
