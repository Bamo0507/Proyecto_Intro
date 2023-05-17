import requests
from email.message import EmailMessage
from data import Data
import ssl
import smtplib
import json
from geopy.geocoders import Nominatim
import datetime

# Revisar las coordenadas de la ubicación del usuario
def check_coordinates(location):
    geolocator = Nominatim(user_agent="my_app")
    location = geolocator.geocode(location)
    latitude = location.latitude
    longitude = location.longitude
    return latitude, longitude

# API keys and endpoints
api_key = "7925925aff4569bdc4ea23ea9c77fa8a"
OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
geolocator = Nominatim(user_agent="my_app")

# Mandar correo al usuario sobre el estado del clima
def send_email(email_receiver, subject, body_message):
    email_data = Data()
    subjet = subject
    if isinstance(body_message, list):
        body = "\n\n".join(body_message)
    else:
        body = body_message
    em = EmailMessage()
    em["From"] = email_data.my_email
    em["To"] = email_receiver
    em["Subject"] = subjet
    em.set_content(body)
    contex = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=contex) as server:
        server.login(email_data.my_email, email_data.password)
        server.sendmail(email_data.my_email, email_receiver, em.as_string())

# Agregar información del usuario
def add_user():

    with open("users.json", "r") as file:
        data = json.load(file)

    name = input("Ingrese su nombre: ")
    email = input("Ingrese su correo: ")
    location = input("A continuar deberá ingresar su ubicación:"
                     "\nDebe ingresar 'Municipio, Departamento'. Por ejemplo, si su ubicación es Fraijanes, escriba 'Fraijanes, Guatemala City': ")
    
    latitude, longitude = check_coordinates(location)

    users = {name: {"email": email, "location": {"ubication":location, "latitude": latitude, "longitude": longitude}}}
    print(users)
    data.update(users)
    with open("users.json", "w") as file:
        json.dump(data, file, indent=4)

#Revisar el clima
def check_weather(latitude, longitude):
    weather_params = {
        "lat":latitude,
        "lon":longitude,
        "appid": api_key,
        "units":"metric",
        "lang":"es"
    }

    response = requests.get(OWM_Endpoint, params=weather_params)

    response.raise_for_status()
    weather_data = response.json()
    current_date = str(datetime.datetime.today())[:10]
    next_day = str(datetime.datetime.today() + datetime.timedelta(days=1))[:10]
    mensajes_hora = []
    fecha = ""

    for i in weather_data["list"]:
        if i["dt_txt"][:10] == current_date:
            fecha = str(i["dt_txt"])
            descripcion = str(i["weather"][0]["description"])
            temp = str(i["main"]["temp"])
            t_max = str(i["main"]["temp_max"])
            t_min = str(i["main"]["temp_min"])
            chance = ""
            if i["pop"] > 0.5:
                chance = "Existen altas probabilidades de lluvia"
            else:
                chance = "No hay altas probabilidades de lluvia"

            mensaje = f"A las {fecha[11:]}:\n La temperatura será  de {temp}°C, con una máxima de {t_max}°C y una mínima de {t_min}°C.\n {chance}\nDescripción de clima: {descripcion}."
            mensajes_hora.append(mensaje)


        elif i["dt_txt"][:10] == next_day:
            fecha = str(i["dt_txt"])
            descripcion = str(i["weather"][0]["description"])
            temp = str(i["main"]["temp"])
            t_max = str(i["main"]["temp_max"])
            t_min = str(i["main"]["temp_min"])
            chance = ""
            if i["pop"] > 0.5:
                chance = "Existen altas probabilidades de lluvia"
            else:
                chance = "No hay altas probabilidades de lluvia"

            mensaje = f"A las {fecha[11:]}:\n La temperatura será  de {temp}°C, con una máxima de {t_max}°C y una mínima de {t_min}°C.\n {chance}, específicamente  {descripcion}."
            mensajes_hora.append(mensaje)
    return mensajes_hora, fecha


