import json

# Importar de um arquivo
with open('json/imobiliaria.json') as json_file:
    parsed_data = json.load(json_file)

# Importar de uma string
json_string = '{"key": "value", "array": [1, 2, 3]}'
parsed_data = json.loads(json_string)

# Escrever em um arquivo:
data = {
    "imobiliaria": [
        {
            "descricao": "Apartamento no centro da cidade",
            "proprietario": {
                "nome": "João Silva",
                "email": "joao.silva@example.com",
                "telefone": ["11987654321"]
            },
            "endereco": {
                "rua": "Rua das Flores",
                "bairro": "Centro",
                "cidade": "São Paulo",
                "numero": "123"
            },
            "caracteristicas": {
                "tamanho": "85m²",
                "numQuartos": 3,
                "numBanheiros": 2
            },
            "valor": 450000
        },
        {
            "descricao": "Casa com quintal grande",
            "proprietario": {
                "nome": "Maria Oliveira",
                "email": "maria.oliveira@example.com",
                "telefone": ["21987654321", "21912345678"]
            },
            "endereco": {
                "rua": "Rua das Acácias",
                "bairro": "Jardim das Flores",
                "cidade": "Rio de Janeiro",
                "numero": "45"
            },
            "caracteristicas": {
                "tamanho": "120m²",
                "numQuartos": 4,
                "numBanheiros": 3
            },
            "valor": 750000
        },
        {
            "descricao": "Kitnet perto da universidade",
            "proprietario": {
                "nome": "Carlos Souza",
                "telefone": ["31987654321"]
            },
            "endereco": {
                "rua": "Avenida Universitária",
                "bairro": "Centro",
                "cidade": "Belo Horizonte"
            },
            "caracteristicas": {
                "tamanho": "30m²",
                "numQuartos": 1,
                "numBanheiros": 1
            },
            "valor": 200000
        },
        {
            "descricao": "Apartamento com vista para o mar",
            "proprietario": {
                "nome": "Ana Pereira",
                "email": "ana.pereira@example.com"
            },
            "endereco": {
                "rua": "Rua da Praia",
                "bairro": "Beira Mar",
                "cidade": "Salvador",
                "numero": "456"
            },
            "caracteristicas": {
                "tamanho": "95m²",
                "numQuartos": 3,
                "numBanheiros": 2
            },
            "valor": 600000
        },
        {
            "descricao": "Sítio com área verde ampla",
            "proprietario": {
                "nome": "Fernando Lima",
                "telefone": ["11999887766"]
            },
            "endereco": {
                "rua": "Estrada do Sítio",
                "bairro": "Zona Rural",
                "cidade": "Campinas"
            },
            "caracteristicas": {
                "tamanho": "500m²",
                "numQuartos": 5,
                "numBanheiros": 4
            },
            "valor": 1500000
        }
    ]
}


with open("parse/imobiliaria.json", "w") as json_file:
    json.dump(data, json_file, indent=4)

# Escrever em uma string:
json_string = json.dumps(data, indent=4)
print(json_string)