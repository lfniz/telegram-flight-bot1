import requests
import telegram
from datetime import datetime, timedelta

# Configuración
TELEGRAM_TOKEN = "8042127217:AAHhW1jCr_UmhWP7v-N10sWmVGNIeG6zGQo"
CHAT_ID = "1659337515"
AMADEUS_CLIENT_ID = "9k8WiSerwvAuOm7LRzHvEy5B5DcjGtss"
AMADEUS_CLIENT_SECRET = "xGl6PMGKiHuo9rY3"

# Obtener token de acceso a Amadeus
def get_access_token():
    url = "https://test.api.amadeus.com/v1/security/oauth2/token"
    data = {
        "grant_type": "client_credentials",
        "client_id": AMADEUS_CLIENT_ID,
        "client_secret": AMADEUS_CLIENT_SECRET
    }
    response = requests.post(url, data=data)
    return response.json().get("access_token")

# Buscar vuelos
def buscar_vuelos(access_token):
    url = "https://test.api.amadeus.com/v2/shopping/flight-offers"
    headers = {"Authorization": f"Bearer {access_token}"}

    resultados = []
    ciudades = ["EZE", "GRU", "GIG"]
    destino = "MAD"
    fecha_salida = (datetime.today() + timedelta(days=10)).strftime("%Y-%m-%d")

    for origen in ciudades:
        params = {
            "originLocationCode": origen,
            "destinationLocationCode": destino,
            "departureDate": fecha_salida,
            "adults": 1,
            "max": 3,
            "currencyCode": "USD"
        }
        response = requests.get(url, headers=headers, params=params)
        data = response.json()
        for oferta in data.get("data", []):
            precio = float(oferta["price"]["total"])
            if precio <= 300:
                salida = oferta["itineraries"][0]["segments"][0]["departure"]["at"]
                resultados.append(f"✈️ {origen} ➡️ {destino} el {salida[:10]} por ${precio} USD")
    return resultados

# Enviar por Telegram
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
