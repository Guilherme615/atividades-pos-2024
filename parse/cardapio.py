from xml.dom.minidom import parse

# Faz o parse do arquivo XML
dom = parse("cardapio.xml")

# Elemento raiz do XML (cardapio)
cardapio = dom.documentElement

# Recebe uma lista dos elementos com tag "prato"
pratos = cardapio.getElementsByTagName('prato')

# Exibe o menu com os IDs e nomes dos pratos
print("Menu:")
for prato in pratos:
    id_prato = prato.getAttribute('id')
    nome = prato.getElementsByTagName('nome')[0].firstChild.nodeValue
    print(f"{id_prato} - {nome}")

# Pergunta ao usuário qual prato deseja saber mais detalhes
escolha = input("\nDigite o ID do prato que deseja saber mais detalhes: ")

# Busca e exibe os detalhes do prato escolhido
for prato in pratos:
    if prato.getAttribute('id') == escolha:
        nome = prato.getElementsByTagName('nome')[0].firstChild.nodeValue
        descricao = prato.getElementsByTagName('descricao')[0].firstChild.nodeValue
        ingredientes = prato.getElementsByTagName('ingrediente')
        preco = prato.getElementsByTagName('preco')[0].firstChild.nodeValue
        calorias = prato.getElementsByTagName('calorias')[0].firstChild.nodeValue
        tempo_preparo = prato.getElementsByTagName('tempoPreparo')[0].firstChild.nodeValue

        print("\nDetalhes do Prato:")
        print(f"Nome: {nome}")
        print(f"Descrição: {descricao}")
        print("Ingredientes:")
        for ingrediente in ingredientes:
            print(f"  - {ingrediente.firstChild.nodeValue}")
        print(f"Preço: {preco}")
        print(f"Calorias: {calorias}")
        print(f"Tempo de Preparo: {tempo_preparo}")
        break
else:
    print("Prato não encontrado!")
