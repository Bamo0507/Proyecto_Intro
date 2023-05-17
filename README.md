# WeatherWatcher

WeatherWatcher es una aplicación que envía correos electrónicos con el reporte del clima a los usuarios registrados. Los usuarios pueden ingresar su nombre, correo electrónico y ubicación para recibir notificaciones diarias sobre el clima en su área.

## Requisitos

- Python 3.x
- Paquetes necesarios:
  - `requests`
  - `email`
  - `ssl`
  - `smtplib`
  - `json`
  - `geopy`

## Configuración

1. Obtén una clave de API de OpenWeatherMap (OWM): [OpenWeatherMap API](https://openweathermap.org/api)

2. Configura tu cuenta de correo electrónico de Gmail:
   - Asegúrate de tener habilitado el acceso de aplicaciones menos seguras en tu cuenta de Gmail. Puedes habilitarlo aquí: [Habilitar acceso de aplicaciones menos seguras](https://myaccount.google.com/lesssecureapps)

3. Crea un archivo `data.py` en el mismo directorio y define la siguiente clase con tus datos de correo electrónico:

```python
class Data:
    my_email = "tu_correo@gmail.com"
    password = "tu_contraseña"
```

## Funcionalidades

### Agregar un usuario

La función `add_user()` permite agregar un usuario al sistema ingresando su nombre, correo electrónico y ubicación. La ubicación debe estar en el formato "Municipio, Departamento", por ejemplo, "Fraijanes, Guatemala City". La función obtiene las coordenadas geográficas (latitud y longitud) de la ubicación utilizando la biblioteca Geopy.

### Enviar correos electrónicos

La función `mandar_correos()` envía correos electrónicos a los usuarios registrados con el reporte del clima de su ubicación. Utiliza la función `check_weather()` para obtener el reporte del clima en función de las coordenadas geográficas de cada usuario.

### Verificar el clima

La función `check_weather(latitude, longitude)` recupera los datos del clima utilizando la API de OpenWeatherMap. Obtiene la fecha actual y la fecha del día siguiente. Luego, recorre los datos del clima y compara las fechas para determinar si corresponden al día actual o al día siguiente. Genera mensajes con información detallada sobre el clima en cada hora relevante y los devuelve como una lista de mensajes y la fecha correspondiente.

### Enviar correo electrónico

La función `send_email(email_receiver, subject, body_message)` crea un mensaje de correo electrónico utilizando la biblioteca `email` y envía el correo electrónico al destinatario utilizando el protocolo SMTP. Permite enviar un mensaje de cuerpo simple o una lista de mensajes con una separación doble de línea.

## Uso

1. Ejecuta el programa y sigue las instrucciones en la consola para agregar usuarios y enviar correos electrónicos.

2. Los usuarios recibirán un correo electrónico diario a las 6 AM con el reporte del clima de su ubicación ingresada.

3. Puedes personalizar los detalles del correo electrónico modificando la función `send_email()`.

4. Recuerda mantener actualizada la lista de usuarios en el archivo `users.json`.

## Notas

- Para utilizar la API de OpenWeatherMap, asegúrate de tener una clave de API válida y reemplaza `api_key` en el código con tu propia clave.

- La biblioteca Geopy utiliza el servicio de geocodificación de Nominatim. Asegúrate de cumplir con los términos de uso de Nominatim al utilizar esta biblioteca.

- Asegúrate de configurar correctamente los datos de tu cuenta de correo electrónico en el archivo `data.py`.

- Puedes modificar la lógica del programa para adaptarla a tus necesidades específicas.

---
