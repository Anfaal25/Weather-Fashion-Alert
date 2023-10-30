import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv
import os
import requests

load_dotenv()


def get_weather(api_key, city):
    weather_url = "http://api.openweathermap.org/data/2.5/weather"
    parameters = {
        "q" : city,
        "appid" : os.getenv('api_key'),
        "units" : "metric",                 # Metric ensures that the Units of Temperature are in Celsius 
    }

    response = requests.get(weather_url, params=parameters)

    if response.status_code == 200:
        data = response.json()
        temperature = data["main"]["temp"]
        weather_description = data["weather"][0]["description"]
        return f"Weather in {city}\nDescription: {weather_description}\nTemperature: {temperature} C"
    else:
        return "Unable to fetch Weather."
    

city = "Calgary"
weather_message = get_weather(os.getenv('api_key'), city)


'''def generate_clothing_recommendation(weather_message):
    prompt = f"Given the weather: {weather_message}, recommend me what clothing I should wear."

    response = openai.Completion.create(
        engine="davinci",
        prompt=prompt,
        max_tokens=50,  # Adjust the length of the response as needed
    )

    return response.choices[0].text

clothing_recommendation = generate_clothing_recommendation(weather_message)'''


def configure():
    load_dotenv()

def send_email(subject, body):
    from_name = "Weather Update"
    msg = MIMEMultipart()
    msg['From'] = f"{from_name} <{os.getenv('from_email')}>"
    msg['To'] = os.getenv('to_email')
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(os.getenv('from_email'), os.getenv('from_email_password'))
    text = msg.as_string()
    server.sendmail(os.getenv('from_email'), os.getenv('to_email'), text)
    server.quit()

subject = ""
body = weather_message

send_email(subject, body)

