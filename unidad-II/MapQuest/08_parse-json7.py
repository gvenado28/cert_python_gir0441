''''
Descripcion: Comprobar si hay una entrada de usuario no válida.
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
    
if json_status == 0:
    print("API Status: " + str(json_status) + " = A successful route call.\n")
    print("Directions from " + (orig) + " to " + (dest))
    print("Trip Duration:   " + str(json_data["route"]['formattedTime']))
    print("Kilometers:      " + str("{:.2f}".format((json_data["route"]["distance"])*1.61)))
    print("Fuel Used (Ltr): " + str("{:.2f}".format((json_data["route"]["fuelUsed"])*3.78)))
    print("=============================================")
    for each in json_data["route"]["legs"][0]["maneuvers"]:
        print((each["narrative"]) + " (" + str("{:.2f}".format((each["distance"])*1.61) + " km)"))
    print("=============================================\n")
elif json_status == 402:
        print("**********************************************")
        print("For Staus Code: " + str(json_status) + "; Invalid user inputs for one or both locations.")
        print("**********************************************\n")
        print("=============================================")
else:
    print("************************************************************************")
    print("For Staus Code: " + str(json_status) + ", Refer to:")
    print("https://developer.mapquest.com/documentation/directions-api/status-codes")
    print("************************************************************************\n")