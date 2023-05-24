import urllib.parse
import requests

main_api = "https://www.mapquestapi.com/directions/v2/route?"
key = "Oz5WH902HQ7uvWz24lOJiDzNRzBoUicw"


while True:
    orig = input("Ciudad de Origen: ")
    if orig == "salir" or orig == "s":
        break
    dest = input("Ciudad de Destino: ")
    if dest == "salir" or dest == "s":
        break

    url = main_api + urllib.parse.urlencode({"key":key, "from":orig, "to":dest, "locale": "es_ES"}) 
    json_data = requests.get(url).json()
    print("URL: " + (url))

    json_data = requests.get(url).json()
    json_status = json_data["info"]["statuscode"]

    if json_status == 0:
        print("Estado de la API: " + str(json_status) + " = una llamada de ruta exitosa.\n")
        print("=============================================")
        print("Direcciones desde: " + (orig) + " hacía " + (dest))
        print("Duración del Viaje:   " + (json_data["route"]["formattedTime"]))
        print("Kilometros:      " + str("{:.2f}".format((json_data["route"]["distance"])*1.61)))
        print("=============================================")
        for each in json_data["route"]["legs"][0]["maneuvers"]:
            print((each["narrative"]) + " (" + str("{:.2f}".format((each["distance"])*1.61) + " km)"))
        print("=============================================\n")
    elif json_status == 402:
        print("******")
        print("Status Code: " + str(json_status) + "; Invalid user inputs for one or both locations.")
        print("******\n")
    elif json_status == 611:
        print("******")
        print("Status Code: " + str(json_status) + "; Missing an entry for one or both locations.")
        print("******\n")
    else:
        print("********")
        print("For Staus Code: " + str(json_status) + "; Refer to:")
        print("https://developer.mapquest.com/documentation/directions-api/status-codes")
        print("********\n")
