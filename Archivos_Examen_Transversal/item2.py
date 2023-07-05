import requests
import os
import sys

api_key = "Oz5WH902HQ7uvWz24lOJiDzNRzBoUicw"
lang = "es_ES"

orig = input("Ciudad de Origen: ").lower()
if orig == "salir" or orig == "s":
    sys.exit()
dest = input("Ciudad de Destino: ").lower()
if dest == "salir" or dest == "s":
    sys.exit()

os.system('clear')

url = f'https://www.mapquestapi.com/directions/v2/route?key={api_key}&from={orig}&to={dest}&locale={lang}'
print(f'URL: {url} \n')
response = requests.get(url)
if response.status_code == 200:
    data = response.json()
    if data['info']['statuscode'] == 0:
        #duracion del viaje
        traveltime = data['route']['formattedTime']
        #dist en millas
        distance = data['route']['distance']
        #codigo de pais de origen y destino respectivamente
        countryorg = data['route']['locations'][0]['adminArea1']
        countrydest = data['route']['locations'][1]['adminArea1']
        #dist en km
        distanceinkm = distance * 1.61

        print(f'Origen: {orig.capitalize()}, {countryorg}')
        print(f'Destino: {dest.capitalize()}, {countrydest}') 
        print(f'Distancia: {"{:.1f}".format(distanceinkm)} Km')
        print(f'Tiempo de viaje: {traveltime} (hh:mm:ss) \n')

        narrativesteps = 0
        #narrativa del viaje
        for each in data["route"]["legs"][0]["maneuvers"]:
            narrativesteps +=1
            print(f"{narrativesteps} | " + (each["narrative"]) + " (" + str("{:.1f}".format((each["distance"])*1.61) + " Km)"))
    elif data['info']['statuscode'] >= 1:
        print(data['info']['messages'][0])
else:
    print('Error en la consulta')
    print(response.status_code)
