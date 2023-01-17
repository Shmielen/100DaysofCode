travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]
#🚨 Do NOT change the code above

#TODO: Write the function that will allow new countries
#to be added to the travel_log. 👇
#again = True
#while again:
#    country = str(input("Which country would you like to add? "))
#    visits = int(input("How many times have you visited? "))
#    city = ""
#    cities = []
#    while city != "no":
#        city = str(input("Add a city"))
#        if city != "no":
#            cities.append(city)

def add_new_country(country, visits, cities):
    new_dict = {}
    new_dict["country"] = country
    new_dict["visits"] = visits
    new_dict["cities"] = cities
    travel_log.append(new_dict)





#🚨 Do not change the code below
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)
