import requests
from email.message import EmailMessage
from data import Data
import ssl
import smtplib
import json
from geopy.geocoders import Nominatim
import datetime


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
