import json

# Importar de um arquivo
with open('json/imobiliaria.json') as json_file:
    parsed_data = json.load(json_file)

# Importar de uma string
json_string = '{"key": "value", "array": [1, 2, 3]}'
parsed_data = json.loads(json_string)

# Escrever em um arquivo:
data = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

with open("parse/imobiliaria.json", "w") as json_file:
    json.dump(data, json_file)

# Escrever em uma string:
json_string = json.dumps(data)