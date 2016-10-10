
def city_country(city, country, population=''):
    if population:
        return str.title(city + ", " + country + " - " + population)
    else:
        return str.title(city + ", " + country)




