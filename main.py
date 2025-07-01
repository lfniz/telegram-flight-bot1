import requests
import telegram
from datetime import datetime, timedelta

# Configuración
TELEGRAM_TOKEN = "8042127217:AAHhW1jCr_UmhWP7v-N10sWmVGNIeG6zGQo"
CHAT_ID = "1659337515"
AMADEUS_CLIENT_ID = "9k8WiSerwvAuOm7LRzHvEy5B5DcjGtss"
AMADEUS_CLIENT_SECRET = "xGl6PMGKiHuo9rY3"

def get_access_token():
    url = "https://test.api.amadeus.com/v1/security/oauth2/token"
    data = {
        "grant_type": "client_credentials",
        "client_id": AMADEUS_CLIENT_ID,
        "client_secret": AMADEUS_CLIENT_SECRET
    }
    response = requests.post(url, data=data)
    return response.json().get("access_token")

def buscar_vuelos(access_token):
    url = "https://test.api.amadeus.com/v2/shopping/flight-offers"
    headers = {"Authorization": f"Bearer {access_token}"}

    resultados = []
    origenes = ["EZE", "GRU", "GIG"]
    destinos = ["MAD", "CDG", "FCO", "LIS"]
    fecha_inicio = datetime(2026, 5, 1)
    fecha_fin = datetime(2026, 8, 31)
    delta = timedelta(days=1)

    fecha_actual = fecha_inicio
    while fecha_actual <= fecha_fin:
        fecha_salida = fecha_actual.strftime("%Y-%m-%d")
        for origen in origenes:
            for destino in destinos:
                for tipo_viaje, limite_precio in [("ONE_WAY", 350), ("ROUND_TRIP", 700)]:
                    params = {
                        "originLocationCode": origen,
                        "destinationLocationCode": destino,
                        "departureDate": fecha_salida,
                        "adults": 1,
                        "max": 2,
                        "currencyCode": "USD"
                    }
                    if tipo_viaje == "ROUND_TRIP":
                        fecha_regreso = (fecha_actual + timedelta(days=14)).strftime("%Y-%m-%d")
                        params["returnDate"] = fecha_regreso

                    response = requests.get(url, headers=headers, params=params)
                    data = response.json()
                    for oferta in data.get("data", []):
                        precio = float(oferta["price"]["total"])
                        if precio <= limite_precio:
                            salida = oferta["itineraries"][0]["segments"][0]["departure"]["at"]
                            info = f"✈️ {origen} ➡️ {destino} el {salida[:10]}"
                            if tipo_viaje == "ROUND_TRIP":
                                regreso = oferta["itineraries"][1]["segments"][-1]["arrival"]["at"]
                                info += f" y vuelta el {regreso[:10]}"
                            info += f" por ${precio} USD ({'ida y vuelta' if tipo_viaje == 'ROUND_TRIP' else 'solo ida'})"
                            resultados.append(info)
        fecha_actual += delta
    return resultados

def enviar_mensaje(mensaje):
    bot = telegram.Bot(token=TELEGRAM_TOKEN)
    bot.send_message(chat_id=CHAT_ID, text=mensaje)

def main():
    token = get_access_token()
    vuelos = buscar_vuelos(token)
    if vuelos:
        for vuelo in vuelos:
            enviar_mensaje(vuelo)

if __name__ == "__main__":
    main()

