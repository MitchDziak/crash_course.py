def city_country(city, country):
    area = city + ", " + country
    return area.title()
    
    
while True:
    print("(Enter 'q' to Quit)")
    city = input("Enter the name of a city: ")
    if city == 'q':
        break
        
    country = input("Enter the name of the country: ")
    if country == 'q':
        break
    
    location = city_country(city, country)
    print('"' + location + '"\n')
