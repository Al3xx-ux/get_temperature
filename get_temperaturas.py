import urllib.request, json 

# URLs para cada ciudad
url_barcelona = "https://api.open-meteo.com/v1/forecast?latitude=41.38879&longitude=2.15899&current=temperature_2m,wind_speed_10m&hourly=temperature_2m,relative_humidity_2m,wind_speed_10m"
url_madrid = "https://api.open-meteo.com/v1/forecast?latitude=40.4167&longitude=3.7033&current=temperature_2m,wind_speed_10m&hourly=temperature_2m,relative_humidity_2m,wind_speed_10m"
url_asturias = "https://api.open-meteo.com/v1/forecast?latitude=43.3619&longitude=-5.8492&current=temperature_2m,wind_speed_10m&hourly=temperature_2m,relative_humidity_2m,wind_speed_10m"

# Función principal
def main():
    print("Bienvenido al programa de consulta del tiempo")
    print("Elija una de las siguientes opciones:")
    print("1. Barcelona")
    print("2. Madrid")
    print("3. Asturias")
    opcion = input("Opción: ")

    match opcion:
        case "1":
            with urllib.request.urlopen(url_barcelona) as datos:
                parseado = json.load(datos)
            print("Temperatura en Barcelona: ", parseado["current"]["temperature_2m"])
            print("Velocidad del viento en Barcelona: ", parseado["current"]["wind_speed_10m"])
            print("Humedad relativa en Barcelona: ", parseado["hourly"]["relative_humidity_2m"][0])
        case "2":
            with urllib.request.urlopen(url_madrid) as datos:
                parseado = json.load(datos)
            print("Temperatura en Madrid: ", parseado["current"]["temperature_2m"])
            print("Velocidad del viento en Madrid: ", parseado["current"]["wind_speed_10m"])
            print("Humedad relativa en Madrid: ", parseado["hourly"]["relative_humidity_2m"][0])
        case "3":
            with urllib.request.urlopen(url_asturias) as datos:
                parseado = json.load(datos)
            print("Temperatura en Asturias: ", parseado["current"]["temperature_2m"])
            print("Velocidad del viento en Asturias: ", parseado["current"]["wind_speed_10m"])
            print("Humedad relativa en Asturias: ", parseado["hourly"]["relative_humidity_2m"][0])
        case _:
            print("Opción no válida")

main()
