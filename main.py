import requests
import configure

location = input("Location : ")

response = requests.get(f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={configure.TOKEN}")


if response:
  response = response.json()

  print(f"""

Weather in {location.title()}

{response["weather"][0]["main"]}

Temprature - {round(response["main"]["temp"] - 273.15 )}° Celcius
Feels Like - {round(response["main"]["feels_like"] - 273.15 )}° Celcius
Humidity - {response["main"]["humidity"]} %
Pressure -  {response["main"]["pressure"]} hPa

  
  """)

else:
  print("An error occured. Please check your location or try again later.")
