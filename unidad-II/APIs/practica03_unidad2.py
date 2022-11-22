'''
Clave API: 66eb66e515bc4470beb521636e338a64
Descripción de la API: 
Autor: German Emiliano Venado Soria
Fecha de creación: 08/Nov/2022
'''

import urllib.parse
import requests

main_api = "https://api.meteum.ai/graphql/query"
key  = "a9b66447-f6d4-4428-ba5a-2ec07a459935"
url  = main_api + urllib.parse.urlencode({"key":key})

headers = {
    "X-Meteum-API-Key": key
}

query = """{
  weatherByPoint(request: { lat: 52.37125, lon: 4.89388 }) {
    now {
      temperature
    }
  }
}"""

response = requests.post('https://api.meteum.ai/graphql/query', headers=headers, json={'query': query})

print(response.content)


json_data = requests.get(url).json()
json_status = json_data["info"]["statuscode"]

if json_status == 0:
    print("API Status: " + str(json_status) + " = A successful route call.\n")
    
while True:
    orig = input("Starting Location: ")
    if orig == "quit" or orig == "q":
        break
    dest = input("Destination: ")
    if dest == "quit" or dest == "q":
        break
    url = main_api + urllib.parse.urlencode({"key": key, "from":orig, "to":dest})
    print("URL: " + (url))