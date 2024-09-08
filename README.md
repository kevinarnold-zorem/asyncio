# Herramienta de Prueba de Carga Web Asíncrona

Este código es una herramienta de prueba de carga web escrita en Python usando `asyncio` y `aiohttp`. El objetivo es enviar una gran cantidad de solicitudes HTTP de manera asíncrona a una URL especificada, simulando una prueba de estrés en un servidor web.

### Explicación del Código:

- Se utiliza `argparse` para permitir al usuario especificar la URL objetivo y el número de solicitudes que desea enviar.
  
  **Argumentos**:
  
  - **`url`**: Es la URL objetivo donde se enviarán las solicitudes.
  - **`--num_requests (-n)`**: Permite definir cuántas solicitudes se enviarán al servidor (por defecto, 1000 solicitudes).

### Función `send_request`:

- Toma una sesión de `aiohttp` y una URL como argumentos.
- Intenta hacer una solicitud GET asíncrona a la URL objetivo y luego imprime el estado de la respuesta (como 200 para éxito o 404 para no encontrado).
- Utiliza `response.read()` para asegurarse de que el contenido de la respuesta se lea completamente.
- Si la solicitud falla, se captura la excepción y se imprime el error.

### Función `main`:

- Crea una sesión asíncrona con `aiohttp.ClientSession`.
- Usa un bucle para crear múltiples tareas de solicitudes asíncronas (una por cada solicitud) usando `asyncio.create_task`.
- Se ejecutan todas las tareas simultáneamente con `asyncio.gather`, lo que permite que todas las solicitudes se realicen de forma asíncrona y paralela.

### Ejecución del Script:

Si el script se ejecuta directamente, se invoca `asyncio.run(main())`, que inicia el ciclo de eventos asíncronos.

## Uso del Script:

Para ejecutar el script y realizar una prueba de carga de 1000 solicitudes, podrías usar:

```bash
python load_test.py https://example.com -n 1000
