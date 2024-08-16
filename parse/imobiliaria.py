import json

# Importar o arquivo JSON
with open('json/imobiliaria.json', encoding='utf-8') as json_file:
    parsed_data = json.load(json_file)

# Corrige a chave do JSON para 'imoveis' em vez de 'imovel'
imoveis = parsed_data["imoveis"]

# Exibe o menu de imóveis
print("Lista de Imóveis:")
id_imovel = 1
for imovel in imoveis:
    print(f"Imóvel {id_imovel}: {imovel['descricao']}")
    id_imovel += 1

print("="*10)

# Solicita ao usuário o ID do imóvel desejado
id_selecionado = int(input("Informe o ID do imóvel: "))
imovel = imoveis[id_selecionado - 1]

# Exibe os detalhes do imóvel selecionado
print("="*10)
print("Descrição geral:")
print(" ° Descrição do Imóvel:", imovel["descricao"])
print(" ° Proprietário(a):", imovel['proprietario']['nome'])

telefones = imovel['proprietario'].get("telefones") or ["Não informado"]
for telefone in telefones:
    print(" ° Telefone:", telefone)

emails = imovel['proprietario'].get("emails") or ["Não informado"]
for email in emails:
    print(" ° Email:", email)

print("\nEndereço do imóvel:")
print(f" ° Rua: {imovel['endereco']['rua']}")
print(f" ° Bairro: {imovel['endereco']['bairro']}")
print(f" ° Cidade: {imovel['endereco']['cidade']}")
print(f" ° Número: {imovel['endereco']['numero'] if imovel['endereco']['numero'] is not None else 'N/A'}")

print("\nCaracterísticas do imóvel:")
print(f" ° Tamanho: {imovel['caracteristicas']['tamanho']} m²")
print(f" ° Quartos: {imovel['caracteristicas']['numQuartos']}")
print(f" ° Banheiros: {imovel['caracteristicas']['numBanheiros']}")

print(f"\nValor geral do Imóvel: R$ {imovel['valor']}")
