'''
Descripción de la API: 
Autor: German Emiliano Venado Soria
Fecha de creación: 08/Nov/2022
'''

import urllib.parse
import requests

main_api = "https://api.meteum.ai/graphql/query"
key  = "a9b66447-f6d4-4428-ba5a-2ec07a459935"
url  = main_api + urllib.parse.urlencode({"key":key})

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