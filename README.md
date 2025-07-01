# Bot de Vuelos Baratos ✈️

Este bot busca vuelos desde Buenos Aires, San Pablo y Río de Janeiro hacia Europa por menos de 300 USD y te los envía por Telegram todos los días.

## ¿Cómo funciona?

Usa la API de Amadeus para buscar vuelos y un bot de Telegram para enviarte los resultados.

### Configuración

1. Crear una cuenta en https://developers.amadeus.com/
2. Obtener tu `client_id` y `client_secret`
3. Crear un bot con @BotFather y obtener tu `TELEGRAM_TOKEN`
4. Obtener tu `chat_id` (ya lo hiciste)

### Despliegue en Render

1. Subí este repositorio a GitHub.
2. Entrá a https://render.com/
3. Elegí "New Web Service" → conecta tu GitHub → elegí este repo.
4. Render detectará automáticamente el `.render.yaml` y lo programará para que corra todos los días.

¡Y listo!

