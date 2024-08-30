import requests
from xml.dom.minidom import parseString

url = "http://webservices.oorsprong.org/websamples.countryinfo/CountryInfoService.wso"

country = input("Digite o código do país: ")
funcao = "CountryFlag"
payload = f"""<?xml version="1.0" encoding="utf-8"?>
<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
  <soap:Body>
    <{funcao} xmlns="http://www.oorsprong.org/websamples.countryinfo">
      <sCountryISOCode>{country}</sCountryISOCode>
    </{funcao}>
  </soap:Body>
</soap:Envelope>"""

headers = {
    'Content-Type': 'text/xml; charset=utf-8'
}

response = requests.post(url, headers=headers, data=payload)

content = parseString(response.text)

result_tag = content.getElementsByTagNameNS('*', f"{funcao}Result")

result = result_tag[0].firstChild.nodeValue
print(f"Bandeira do país: {result}")

