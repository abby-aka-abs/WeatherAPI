import requests

user_ct = input("Enter the name of the city: ")
user_lat = input("Enter lattitude of city: ")
user_lon = input("Enter longitude of city: ")
user_units = input("Enter units: ")


class City:
    def __init__(self,name,lat,lon,units="metric"):
        self.name = name
        self.lat = lat
        self.lon = lon
        self.units = units
        self.get_data()
        self.print_temp()
    
    def get_data(self):
        try: 
            response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?units={self.units}&lat={self.lat}&lon={self.lon}&appid=237cfe60ec205900347be41727a3fbe8")
            
        except Exception as e:
            print("Please connect to internet")
            print(e)
            
        self.response_json = response.json()
        self.temp = self.response_json["main"]["temp"]
        self.temp_min = self.response_json["main"]["temp_min"] 
        self.temp_max = self.response_json["main"]["temp_max"]

    def print_temp(self):
        self.temp_units = "Celsius"
        if self.units == "imperial":
            self.temp_units = "Farenheit"

        print(f"In {self.name} it is currently {self.temp} degrees {self.temp_units}")
        print(f"Todays High: {self.temp_max} degrees {self.temp_units}")
        print(f"Todays Low: {self.temp_min} degrees {self.temp_units}")

my_city = City(user_ct, user_lat, user_lon,user_units)

