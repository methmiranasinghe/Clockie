
# import tkinter as tk
# from tkinter import ttk
# from datetime import datetime
# import requests

# class GlobalClockApp:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("Global Clock")

#         self.city_label = ttk.Label(root, text="Enter City:")
#         self.city_label.grid(row=0, column=0, padx=10, pady=10)

#         self.city_entry = ttk.Entry(root)
#         self.city_entry.grid(row=0, column=1, padx=10, pady=10)

#         self.get_time_button = ttk.Button(root, text="Get Time", command=self.get_time)
#         self.get_time_button.grid(row=0, column=2, padx=10, pady=10)

#         self.time_label = ttk.Label(root, text="")
#         self.time_label.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

#     def get_time(self):
#         city = self.city_entry.get()
#         if city:
#             time = self.fetch_time(city)
#             if time:
#                 self.time_label.config(text=f"The current time in {city} is {time}")
#             else:
#                 self.time_label.config(text=f"Error fetching time for {city}")
#         else:
#             self.time_label.config(text="Please enter a city")

#     def fetch_time(self, city):
#         try:
#             # Use the WorldTimeAPI to get the current time for the given city
#             response = requests.get(f"http://worldtimeapi.org/api/timezone/asia/{city}")
#             data = response.json()
#             time_str = data['datetime']

#             # Convert time to a datetime object
#             dt = datetime.strptime(time_str, "%Y-%m-%dT%H:%M:%S.%f%z")

#             return dt.strftime("%Y-%m-%d %H:%M:%S")
#         except Exception as e:
#             print(f"Error fetching time: {e}")
#             return None

# if __name__ == "__main__":
#     root = tk.Tk()
#     app = GlobalClockApp(root)
#     root.mainloop()



# import tkinter as tk
# from tkinter import ttk
# from datetime import datetime
# import requests

# class GlobalClockApp:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("Global Clock")

#         self.city_label = ttk.Label(root, text="Enter City:")
#         self.city_label.grid(row=0, column=0, padx=10, pady=10)

#         self.city_entry = ttk.Entry(root)
#         self.city_entry.grid(row=0, column=1, padx=10, pady=10)

#         self.get_time_button = ttk.Button(root, text="Get Time", command=self.get_time)
#         self.get_time_button.grid(row=0, column=2, padx=10, pady=10)

#         self.time_label = ttk.Label(root, text="")
#         self.time_label.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

#     def get_time(self):
#         city = self.city_entry.get()
#         if city:
#             country = self.get_country(city)
#             if country:
#                 time = self.fetch_time(city, country)
#                 if time:
#                     self.time_label.config(text=f"The current time in {city}, {country} is {time}")
#                 else:
#                     self.time_label.config(text=f"Error fetching time for {city}")
#             else:
#                 self.time_label.config(text=f"Error fetching country for {city}")
#         else:
#             self.time_label.config(text="Please enter a city")

#     def get_country(self, city):
#         try:
#             # Use the Geonames API to get country information based on the city
#             geonames_api_username = "methmi12"  # Replace with your Geonames username
#             response = requests.get(
#                 f"http://api.geonames.org/searchJSON?q={city}&maxRows=1&type=json&username={geonames_api_username}"
#             )
#             data = response.json()
#             country = data['geonames'][0]['countryName']
#             return country
#         except Exception as e:
#             print(f"Error fetching country: {e}")
#             return None

#     def fetch_time(self, city, country):
#         try:
#             # Use the WorldTimeAPI to get the current time for the given city and country
#             response = requests.get(f"http://worldtimeapi.org/api/timezone/{country}/{city}")
#             data = response.json()
#             time_str = data['datetime']

#             # Convert time to a datetime object
#             dt = datetime.strptime(time_str, "%Y-%m-%dT%H:%M:%S.%f%z")

#             return dt.strftime("%Y-%m-%d %H:%M:%S")
#         except Exception as e:
#             print(f"Error fetching time: {e}")
#             return None

# if __name__ == "__main__":
#     root = tk.Tk()
#     app = GlobalClockApp(root)
#     root.mainloop()
import tkinter as tk
from tkinter import ttk
from datetime import datetime
import requests

class GlobalClockApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Global Clock")

        self.city_label = ttk.Label(root, text="Enter City:")
        self.city_label.grid(row=0, column=0, padx=10, pady=10)

        self.city_entry = ttk.Entry(root)
        self.city_entry.grid(row=0, column=1, padx=10, pady=10)

        self.get_time_button = ttk.Button(root, text="Get Time", command=self.get_time)
        self.get_time_button.grid(row=0, column=2, padx=10, pady=10)

        self.time_label = ttk.Label(root, text="")
        self.time_label.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

    def get_time(self):
        city = self.city_entry.get()
        if city:
            continent = self.get_continent(city)
            if continent:
                time = self.fetch_time(city, continent)
                if time:
                    self.time_label.config(text=f"The current time in {city}, {continent} is {time}")
                else:
                    self.time_label.config(text=f"Error fetching time for {city}")
            else:
                self.time_label.config(text=f"Error fetching continent for {city}")
        else:
            self.time_label.config(text="Please enter a city")

    def get_continent(self, city):
        try:
            # Use the Geonames API to get country information based on the city
            geonames_api_username = "methmi12"
            response = requests.get(
                f"http://api.geonames.org/searchJSON?q={city}&maxRows=1&type=json&username={geonames_api_username}"
            )
            data = response.json()
            
            # Attempt to extract continent information from the Geonames "countryInfo" endpoint
            if 'geonames' in data and data['geonames']:
                country_code = data['geonames'][0].get('countryCode')
                continent = self.get_continent_from_country_code(country_code)
                return continent
            else:
                return "Unknown"
        except Exception as e:
            print(f"Error fetching continent: {e}")
            return None

    def get_continent_from_country_code(self, country_code):
        try:
            # Use the Geonames "countryInfo" API to get continent information based on country code
            geonames_api_username = "methmi12"
            response = requests.get(
                f"http://api.geonames.org/countryInfoJSON?country={country_code}&username={geonames_api_username}"
            )
            data = response.json()
            
            # Extract continent from the response
            if 'geonames' in data and data['geonames']:
                continent = data['geonames'][0].get('continentName')
                
                return continent
            else:
                return "Unknown"
        except Exception as e:
            print(f"Error fetching continent from country code: {e}")
            return None

    def fetch_time(self, city, continent):
        try:
            # Use the WorldTimeAPI to get the current time for the given city and continent
            response = requests.get(f"http://worldtimeapi.org/api/timezone/{continent}/{city}")
            data = response.json()

            # The 'datetime' key may not exist in the response
            if 'datetime' in data:
                time_str = data['datetime']

                # Convert time to a datetime object
                dt = datetime.strptime(time_str, "%Y-%m-%dT%H:%M:%S.%f%z")

                return dt.strftime("%Y-%m-%d %H:%M:%S")
            else:
                return None
        except Exception as e:
            print(f"Error fetching time: {e}")
            return None

if __name__ == "__main__":
    root = tk.Tk()
    app = GlobalClockApp(root)
    root.mainloop()
