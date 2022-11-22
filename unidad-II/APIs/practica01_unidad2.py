'''
Clave API: 66eb66e515bc4470beb521636e338a64
Descripción de la API: 
Autor: German Emiliano Venado Soria
Fecha de creación: 08/Nov/2022
'''

import urllib.parse
import requests

url = "https://api.covidtracking.com/v1/states/ca/20200501.json"
'''key  = ""
url  = main_api + urllib.parse.urlencode({"key":key})'''

json_data = requests.get(url).json()
json_status = json_data["date"]

if json_status == 20200501:
    json_status = "01/05/2020"
    print("API Date: " + str(json_status) + " = A successful route call.\n")
    
while True:
    orig = input("Starting Location: ")
    if orig == "quit" or orig == "q":
        break
    dest = input("Destination: ")
    if dest == "quit" or dest == "q":
        break
    url = url + urllib.parse.urlencode({"from":orig, "to":dest})
    print("URL: " + (url))
    print("Directions from " + (orig) + " to " + (dest))
    print("Estado:       " + str(json_data["state"])) 
    print("=============================================")