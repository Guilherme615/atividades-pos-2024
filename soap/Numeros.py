from zeep import Client

# URL do WSDL
wsdl = "https://www.dataaccess.com/webservicesserver/NumberConversion.wso?WSDL"

# Criando o cliente SOAP
client = Client(wsdl=wsdl)

# Solicita ao usuário para digitar um número
number = int(input("Digite um número: "))

# Chamada ao método NumberToWords
response = client.service.NumberToWords(ubiNum=number)

# Imprime o resultado por extenso
print(f"O número {number} por extenso é: {response}")
