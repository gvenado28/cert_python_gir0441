''''
Descripcion: Agregar entrada de usuario para preguntar por la dirección de origen y destino.
Autor: German Venado
Fecha: 20 nov 2022
'''

import urllib.parse
import requests

main_api = "https://www.mapquestapi.com/directions/v2/route?"
key  = "A3c5VKgp7bxrii349w3GJbqoJcqEJN95"
url  = main_api + urllib.parse.urlencode({"key":key})

json_data = requests.get(url).json()
print(json_data)

json_data = requests.get(url).json()
json_status = json_data["info"]["statuscode"]

if json_status == 0:
    print("API Status: " + str(json_status) + " = A successful route call.\n")
    
while True:
    orig = input("Starting Location: ")
    dest = input("Destination: ")
    url = main_api + urllib.parse.urlencode({"key": key, "from":orig, "to":dest})
    print("URL: " + (url))