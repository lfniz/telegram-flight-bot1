# Bot de Vuelos Baratos ✈️

Este bot busca vuelos desde Buenos Aires, San Pablo y Río de Janeiro hacia Europa por menos de 300 USD y te los envía por Telegram todos los días.

## ¿Cómo funciona?

Usa la API de Amadeus para buscar vuelos y un bot de Telegram para enviarte los resultados.

### Configuración

1. Crear una cuenta en https://developers.amadeus.com/
2. Obtener tu `client_id` y `client_secret`
3. Crear un bot con @BotFather y obtener tu `TELEGRAM_TOKEN`
4. Obtener tu `chat_id`

### Despliegue en Render

1. Subí este repositorio a GitHub.
2. Entrá a https://render.com/
3. Elegí "New Background Worker" → conecta tu GitHub → elegí este repo.
4. Configurá los siguientes valores:
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `python main.py`
   - **Schedule**: `0 12 * * *` (una vez al día)
   - Variables de entorno:
     - TELEGRAM_TOKEN
     - CHAT_ID
     - AMADEUS_CLIENT_ID
     - AMADEUS_CLIENT_SECRET

¡Y listo!
