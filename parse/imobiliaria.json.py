from xml.dom.minidom import parse
import json

# Parse do arquivo XML da imobiliária
dom = parse("xml/imobiliaria.xml")
imobiliaria = dom.documentElement
imoveis = imobiliaria.getElementsByTagName("imovel")

# Estrutura para armazenar os dados extraídos
data = {"imoveis": []}

# Extração dos dados
for imovel in imoveis:
    descricao = imovel.getElementsByTagName("descricao")[0].firstChild.nodeValue

    proprietario = imovel.getElementsByTagName("proprietario")[0]
    nome_proprietario = proprietario.getElementsByTagName("nome")[0].firstChild.nodeValue
    
    telefones_proprietario = proprietario.getElementsByTagName("telefone")
    telefones = [telefone.firstChild.nodeValue for telefone in telefones_proprietario]
    
    emails_proprietario = proprietario.getElementsByTagName("email")
    emails = [email.firstChild.nodeValue for email in emails_proprietario]
    
    endereco = imovel.getElementsByTagName("endereco")[0]
    rua = endereco.getElementsByTagName("rua")[0].firstChild.nodeValue
    bairro = endereco.getElementsByTagName("bairro")[0].firstChild.nodeValue
    cidade = endereco.getElementsByTagName("cidade")[0].firstChild.nodeValue
    
    numero_do_imovel = imovel.getElementsByTagName("numero")
    numero = numero_do_imovel[0].firstChild.nodeValue.strip() if numero_do_imovel and numero_do_imovel[0].firstChild else None

    caracteristicas = imovel.getElementsByTagName("caracteristicas")[0]
    
    # Remove 'm²' da string do tamanho antes de converter para float
    tamanho = float(caracteristicas.getElementsByTagName("tamanho")[0].firstChild.nodeValue.replace("m²", "").strip())
    numQuartos = int(caracteristicas.getElementsByTagName("numQuartos")[0].firstChild.nodeValue)
    numBanheiros = int(caracteristicas.getElementsByTagName("numBanheiros")[0].firstChild.nodeValue)

    valor = float(imovel.getElementsByTagName("valor")[0].firstChild.nodeValue)

    data["imoveis"].append({
        "descricao": descricao,
        "proprietario": {
            "nome": nome_proprietario,
            "telefones": telefones,
            "emails": emails
        },
        "endereco": {
            "rua": rua,
            "bairro": bairro,
            "cidade": cidade,
            "numero": numero
        },
        "caracteristicas": {
            "tamanho": tamanho,
            "numQuartos": numQuartos,
            "numBanheiros": numBanheiros
        },
        "valor": valor
    })

# Salva os dados extraídos em um arquivo JSON
with open("json/imobiliaria.json", "w", encoding="utf-8") as json_file:
    json.dump(data, json_file, ensure_ascii=False, indent=2)

print("Arquivo imobiliaria.json gerado com sucesso!")
