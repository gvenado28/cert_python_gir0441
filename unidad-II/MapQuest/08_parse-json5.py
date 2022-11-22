''''
Descripcion: Analizar y mostrar datos del diccionario de route.
Autor: German Venado
Fecha: 20 nov 2022
'''

import urllib.parse
import requests

main_api = "https://www.mapquestapi.com/directions/v2/route?"
key  = "A3c5VKgp7bxrii349w3GJbqoJcqEJN95"
url  = main_api + urllib.parse.urlencode({"key":key})

json_data = requests.get(url).json()
'''print(json_data)'''
json_status = json_data["info"]["statuscode"]
    
while True:
    orig = input("Starting Location: ")
    if orig == "quit" or orig == "q":
        break
    dest = input("Destination: ")
    if dest == "quit" or dest == "q":
        break
    url = main_api + urllib.parse.urlencode({"key": key, "from":orig, "to":dest})
    print("URL: " + (url))
    

    print("API Status: " + str(json_status) + " = A successful route call.\n")
    print("Directions from " + (orig) + " to " + (dest))
    print("Trip Duration:   " + str(json_data["route"]['formattedTime']))
    print("Kilometers:      " + str("{:.2f}".format((json_data["route"]["distance"])*1.61)))
    print("Fuel Used (Ltr): " + str("{:.2f}".format((json_data["route"]["fuelUsed"])*3.78)))
    print("=============================================")