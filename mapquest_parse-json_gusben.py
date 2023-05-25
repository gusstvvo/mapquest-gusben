import urllib.parse
import requests

def traducir_texto(texto):
    # Lógica para traducir el texto al español
    return texto

def obtener_distancia(orig, dest):
    main_api = "https://www.mapquestapi.com/directions/v2/route?"
    key = "jHuBoLHDqAXksv4ibAuhTFH06OJoAwOF"

    parametros = {
        "key": key,
        "from": orig,
        "to": dest,
        "locale": "es_ES"
    }
    url = main_api + urllib.parse.urlencode(parametros)
    json_data = requests.get(url).json()

    distancia = json_data["route"]["distance"]
    return distancia

def obtener_duracion(orig, dest):
    main_api = "https://www.mapquestapi.com/directions/v2/route?"
    key = "jHuBoLHDqAXksv4ibAuhTFH06OJoAwOF"

    parametros = {
        "key": key,
        "from": orig,
        "to": dest,
        "locale": "es_ES"
    }
    url = main_api + urllib.parse.urlencode(parametros)
    json_data = requests.get(url).json()

    duracion_segundos = json_data["route"]["time"]
    horas = duracion_segundos // 3600
    minutos = (duracion_segundos % 3600) // 60
    segundos = duracion_segundos % 60

    return horas, minutos, segundos

def mostrar_narrativa(orig, dest):
    main_api = "https://www.mapquestapi.com/directions/v2/route?"
    key = "Oz5WH902HQ7uvWz24lOJiDzNRzBoUicw"

    parametros = {
        "key": key,
        "from": orig,
        "to": dest,
        "locale": "es_ES"
    }
    url = main_api + urllib.parse.urlencode(parametros)
    json_data = requests.get(url).json()

    print("Narrativa del viaje:")
    for step in json_data["route"]["legs"][0]["maneuvers"]:
        narrative = step["narrative"]
        print(traducir_texto(narrative))

def main():
    while True:
        orig = input("Ciudad de Origen: ")
        if orig.lower() == "s":
            break
        dest = input("Ciudad de Destino: ")
        if dest.lower() == "s":
            break

        distancia = obtener_distancia(orig, dest)
        duracion_horas, duracion_minutos, duracion_segundos = obtener_duracion(orig, dest)

        print("Distancia entre", orig, "y", dest, ": {:.2f} km".format(distancia))
        print("Duración del viaje: {} horas, {} minutos, {} segundos".format(duracion_horas, duracion_minutos, duracion_segundos))

        mostrar_narrativa(orig, dest)

if __name__ == "__main__":
    main()
