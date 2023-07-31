import requests

API_KEY = 'b6907d289e10d714a6e88b30761fae22'
BASE_URL = 'https://samples.openweathermap.org/data/2.5/forecast/hourly?q=London,us&appid=' + API_KEY

def get_weather_data():
    response = requests.get(BASE_URL)
    data = response.json()
    return data

def display_weather():
    weather_data = get_weather_data()
    if 'message' in weather_data:
        print(f"Error: {weather_data['message']}")
    else:
        print("Weather in London, Kentucky:", end=" ")
        for forecast in weather_data['list']:
            date_time = forecast['dt_txt']
            temperature = forecast['main']['temp']
            print(f"Date/Time: {date_time}, Temperature: {temperature} K,", end=" ")

def display_wind_speed():
    weather_data = get_weather_data()
    if 'message' in weather_data:
        print(f"Error: {weather_data['message']}")
    else:
        print("Wind Speed in London, Kentucky:", end=" ")
        for forecast in weather_data['list']:
            date_time = forecast['dt_txt']
            wind_speed = forecast['wind']['speed']
            print(f"Date/Time: {date_time}, Wind Speed: {wind_speed} m/s,", end=" ")

def display_pressure():
    weather_data = get_weather_data()
    if 'message' in weather_data:
        print(f"Error: {weather_data['message']}")
    else:
        print("Pressure in London, Kentucky:", end=" ")
        for forecast in weather_data['list']:
            date_time = forecast['dt_txt']
            pressure = forecast['main']['pressure']
            print(f"Date/Time: {date_time}, Pressure: {pressure} hPa,", end=" ")

def main():
    print("Weather Data Program")
    while True:
        print("\nOptions:")
        print("1. Get weather forecast for London, Kentucky")
        print("2. Get Wind Speed in London, Kentucky")
        print("3. Get Pressure in London, Kentucky")
        print("0. Exit")

        choice = input("Enter your choice (0-3): ")

        if choice == '0':
            print("Exiting the program.")
            break
        elif choice == '1':
            display_weather()
        elif choice == '2':
            display_wind_speed()
        elif choice == '3':
            display_pressure()
        else:
            print("Invalid choice. Please enter a valid option (0-3).")

if __name__ == "__main__":
    main()
